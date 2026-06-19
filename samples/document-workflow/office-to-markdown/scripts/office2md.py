#!/usr/bin/env python3
"""
Office ファイルを Markdown に変換する。

処理方針:
  a (デフォルト) : MarkItDown でテキスト・表のみ変換。グラフは空プレースホルダーになる。
  b              : MarkItDown + OpenAI vision で画像を説明文に変換。API キー必要。
  c              : 画像を PNG として抽出し、Markdown に実ファイル参照を埋め込む。

使い方:
  python office2md.py 仕様書.docx
  python office2md.py 仕様書.docx -o docs/仕様書.md --mode b
  python office2md.py データ.xlsx --mode c --images-dir assets/images
"""

import base64
import io
import re
import sys
import argparse
import logging
import subprocess
import zipfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {
    ".docx", ".xlsx", ".pptx", ".pdf",
    ".html", ".csv", ".json", ".xml", ".epub",
}


# ---------------------------------------------------------------------------
# 方針 A: テキストのみ変換
# ---------------------------------------------------------------------------

def convert_mode_a(input_path: Path, output_path: Path) -> None:
    try:
        from markitdown import MarkItDown
    except ImportError:
        raise RuntimeError("markitdown が未インストールです: pip install markitdown")

    md = MarkItDown()
    result = md.convert(str(input_path))
    output_path.write_text(result.text_content, encoding="utf-8")
    log.info(f"変換完了 (方針A): {output_path}")


# ---------------------------------------------------------------------------
# 方針 B: LLM ビジョンで画像を説明文に変換
# ---------------------------------------------------------------------------

def convert_mode_b(input_path: Path, output_path: Path, llm_model: str) -> None:
    import os
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY 環境変数が設定されていません。\n"
            "  Windows: $env:OPENAI_API_KEY = 'sk-...'\n"
            "  macOS/Linux: export OPENAI_API_KEY=sk-..."
        )
    try:
        from openai import OpenAI
    except ImportError:
        raise RuntimeError("openai が未インストールです: pip install openai")
    try:
        from markitdown import MarkItDown
    except ImportError:
        raise RuntimeError("markitdown が未インストールです: pip install markitdown")

    client = OpenAI(api_key=api_key)
    md = MarkItDown(llm_client=client, llm_model=llm_model)
    result = md.convert(str(input_path))
    output_path.write_text(result.text_content, encoding="utf-8")
    log.info(f"変換完了 (方針B, モデル: {llm_model}): {output_path}")


# ---------------------------------------------------------------------------
# 方針 C: 画像を PNG として抽出し、実ファイル参照を埋め込む
# ---------------------------------------------------------------------------

def _extract_from_docx(input_path: Path, images_dir: Path) -> list[Path]:
    """Word (.docx) の ZIP 内 word/media/ から画像を抽出する。"""
    images_dir.mkdir(parents=True, exist_ok=True)
    extracted: list[Path] = []

    with zipfile.ZipFile(input_path) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
        for name in media:
            dest = images_dir / Path(name).name
            dest.write_bytes(z.read(name))
            extracted.append(dest)
            log.info(f"  抽出: {dest.name}")

    return extracted


def _extract_from_xlsx(input_path: Path, images_dir: Path) -> list[Path]:
    """Excel (.xlsx) を LibreOffice ヘッドレスで PNG にレンダリングする。"""
    images_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["libreoffice", "--headless", "--convert-to", "png",
         str(input_path), "--outdir", str(images_dir)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"LibreOffice 変換失敗 (returncode={result.returncode}):\n{result.stderr}"
        )
    extracted = sorted(images_dir.glob("*.png"))
    log.info(f"  Excel から {len(extracted)} 件を抽出")
    return extracted


def _embed_image_refs(output_path: Path, extracted: list[Path]) -> int:
    """出力 Markdown の空プレースホルダーを実ファイル参照に置き換える。"""
    text = output_path.read_text(encoding="utf-8")
    replaced = 0
    for i, img_path in enumerate(extracted):
        rel = img_path.relative_to(output_path.parent).as_posix()
        before = text
        # 最初に見つかった空プレースホルダーを1件ずつ置換
        text = text.replace("![image]()", f"![図{i + 1}]({rel})", 1)
        if text != before:
            replaced += 1
    output_path.write_text(text, encoding="utf-8")
    return replaced


def convert_mode_c(input_path: Path, output_path: Path, images_dir: Path) -> None:
    suffix = input_path.suffix.lower()

    if suffix == ".docx":
        extracted = _extract_from_docx(input_path, images_dir)
    elif suffix == ".xlsx":
        extracted = _extract_from_xlsx(input_path, images_dir)
    else:
        log.warning(f"方針C: {suffix} の画像抽出は未対応。方針Aにフォールバックします。")
        convert_mode_a(input_path, output_path)
        return

    # テキスト部分を方針 A で変換してから画像参照を埋め込む
    convert_mode_a(input_path, output_path)

    if extracted:
        replaced = _embed_image_refs(output_path, extracted)
        log.info(f"変換完了 (方針C): 画像 {len(extracted)} 件抽出, {replaced} 件埋め込み → {output_path}")
    else:
        log.warning("画像が検出されませんでした。テキスト変換のみ完了しました。")


# ---------------------------------------------------------------------------
# 埋め込み base64 画像の抽出
# ---------------------------------------------------------------------------

# 実 base64 データ: data:image/x-emf;base64,AAAA...
_REAL_BASE64_RE = re.compile(
    r'(!\[([^\]]*)\])\(data:image/([^;]+);base64,([A-Za-z0-9+/=\r\n\s]+?)\)',
    re.DOTALL,
)
# MarkItDown が出力する短縮形: data:image/x-emf;base64...)
_TRUNCATED_RE = re.compile(
    r'(!\[([^\]]*)\])\(data:image/([^;]+);base64\.\.\.\)'
)


def _is_command_available(cmd: str) -> bool:
    """コマンドが PATH に存在するか確認する。"""
    try:
        subprocess.run([cmd, "--version"], capture_output=True, timeout=10)
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _install_imagemagick() -> bool:
    """
    プラットフォームに応じて ImageMagick をインストールする。
    成功したら True を返す。
    """
    import platform
    os_name = platform.system()

    install_cmds: dict[str, list[list[str]]] = {
        "Windows": [["winget", "install", "--id", "ImageMagick.ImageMagick", "-e", "--silent"]],
        "Darwin":  [["brew", "install", "imagemagick"]],
        "Linux":   [
            ["apt-get", "install", "-y", "imagemagick"],   # Debian/Ubuntu
            ["dnf",     "install", "-y", "ImageMagick"],   # Fedora/RHEL
            ["pacman",  "-S",  "--noconfirm", "imagemagick"],  # Arch
        ],
    }

    cmds = install_cmds.get(os_name, [])
    if not cmds:
        log.warning(f"ImageMagick の自動インストールは {os_name} に未対応です。")
        return False

    for cmd in cmds:
        pkg_manager = cmd[0]
        if not _is_command_available(pkg_manager):
            continue
        log.info(f"ImageMagick をインストール中 ({' '.join(cmd)}) ...")
        r = subprocess.run(cmd, capture_output=False, timeout=300)
        if r.returncode == 0:
            log.info("ImageMagick のインストールが完了しました。")
            return True
        log.warning(f"{pkg_manager} でのインストールに失敗しました (exit={r.returncode})。")

    log.error("ImageMagick を自動インストールできませんでした。手動でインストールしてください。")
    return False


def _try_convert_to_png(raw_path: Path, auto_install: bool = False) -> Path | None:
    """EMF 等を PNG に変換する。成功したら PNG のパスを返し raw_path を削除する。"""
    if raw_path.suffix.lower() == ".png":
        return raw_path  # すでに PNG — 変換不要

    png_path = raw_path.with_suffix(".png")

    # 1. Pillow（jpeg, gif, webp, bmp, tiff など標準フォーマット）
    try:
        from PIL import Image
        img = Image.open(raw_path)
        img.save(png_path, "PNG")
        raw_path.unlink()
        log.info(f"  PNG 変換成功 (Pillow): {png_path.name}")
        return png_path
    except Exception:
        pass

    # 2. ImageMagick CLI（EMF/WMF 等）
    magick_available = _is_command_available("magick")
    if not magick_available and auto_install:
        log.info("ImageMagick が見つかりません。自動インストールを試みます...")
        magick_available = _install_imagemagick()

    if magick_available:
        try:
            r = subprocess.run(
                ["magick", str(raw_path), str(png_path)],
                capture_output=True, timeout=30,
            )
            if r.returncode == 0 and png_path.exists():
                raw_path.unlink()
                log.info(f"  PNG 変換成功 (ImageMagick): {png_path.name}")
                return png_path
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

    # 3. Inkscape CLI（SVG/EMF）
    try:
        r = subprocess.run(
            ["inkscape", f"--export-filename={png_path}", "--export-type=png", str(raw_path)],
            capture_output=True, timeout=30,
        )
        if r.returncode == 0 and png_path.exists():
            raw_path.unlink()
            log.info(f"  PNG 変換成功 (Inkscape): {png_path.name}")
            return png_path
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    return None  # 変換できなかった


def _extract_xlsx_media(original_path: Path, images_dir: Path, auto_install: bool = False) -> list[Path]:
    """xlsx ZIP から xl/media/ の画像を取り出し、必要なら PNG に変換して返す。"""
    images_dir.mkdir(parents=True, exist_ok=True)
    extracted: list[Path] = []
    with zipfile.ZipFile(original_path) as z:
        media = sorted(n for n in z.namelist() if n.startswith("xl/media/"))
        if not media:
            return []
        for name in media:
            dest = images_dir / Path(name).name
            dest.write_bytes(z.read(name))
            log.info(f"  ZIP 抽出 (xlsx): {dest.name}")
            final = _try_convert_to_png(dest, auto_install=auto_install) or dest
            extracted.append(final)
    return extracted


def _extract_docx_media(original_path: Path, images_dir: Path) -> list[Path]:
    """docx ZIP から word/media/ の画像を順番に取り出す。"""
    images_dir.mkdir(parents=True, exist_ok=True)
    extracted: list[Path] = []
    with zipfile.ZipFile(original_path) as z:
        for name in sorted(n for n in z.namelist() if n.startswith("word/media/")):
            dest = images_dir / Path(name).name
            dest.write_bytes(z.read(name))
            extracted.append(dest)
            log.info(f"  ZIP 抽出: {dest.name}")
    return extracted


def extract_embedded_images(
    md_path: Path,
    images_dir: Path,
    original_path: Path | None = None,
    auto_install: bool = False,
) -> int:
    """
    Markdown 内の埋め込み画像参照をファイルに保存し、参照を書き換える。

    対応する2パターン:
      - 実 base64:   ![alt](data:image/png;base64,AAAA...)
      - 短縮形:      ![alt](data:image/x-emf;base64...)   ← MarkItDown の出力
        短縮形は original_path（docx）の ZIP から順番にマッピングする。

    返り値: 処理した画像の件数
    """
    text = md_path.read_text(encoding="utf-8")
    images_dir.mkdir(parents=True, exist_ok=True)

    total = 0
    counter: dict[str, int] = {}

    # ── 実 base64 の処理 ──────────────────────────────────────
    def _replace_real(m: re.Match) -> str:
        nonlocal total
        alt  = m.group(2)
        fmt  = m.group(3).replace("x-", "")
        b64  = m.group(4).replace("\n", "").replace(" ", "")
        data = base64.b64decode(b64)

        safe = re.sub(r"[^\w-]", "_", alt).strip("_") or "image"
        counter[safe] = counter.get(safe, 0) + 1
        sfx  = f"_{counter[safe]}" if counter[safe] > 1 else ""
        raw  = images_dir / f"{safe}{sfx}.{fmt}"
        raw.write_bytes(data)

        final = _try_convert_to_png(raw, auto_install=auto_install) or raw
        if final == raw:
            log.warning(f"  PNG 変換不可、元形式のまま保存: {raw.name}")

        total += 1
        return f"![{alt}]({str(final.relative_to(md_path.parent))})"

    text = _REAL_BASE64_RE.sub(_replace_real, text)

    # ── 短縮形の処理（docx ZIP から順番にマッピング）──────────
    truncated_count = len(_TRUNCATED_RE.findall(text))
    if truncated_count > 0:
        if original_path and original_path.suffix.lower() == ".docx":
            media_files = _extract_docx_media(original_path, images_dir)
            log.info(f"短縮形プレースホルダー {truncated_count} 件を ZIP 抽出画像にマッピングします。")

            idx = 0
            def _replace_truncated(m: re.Match) -> str:
                nonlocal idx, total
                alt = m.group(2)

                if idx < len(media_files):
                    raw = media_files[idx]
                    idx += 1
                    final = _try_convert_to_png(raw, auto_install=auto_install) or raw
                    if final == raw:
                        log.warning(f"  PNG 変換不可: {raw.name}")
                    total += 1
                    return f"![{alt}]({str(final.relative_to(md_path.parent))})"
                else:
                    log.warning(f"  ZIP 内に対応する画像がありません: alt='{alt}'")
                    return m.group(0)

            text = _TRUNCATED_RE.sub(_replace_truncated, text)

            # プレースホルダーにマッピングされなかった画像も PNG 変換する
            for remaining in media_files[idx:]:
                if remaining.exists():  # マッピング済みは unlink 済みのため存在チェック
                    converted = _try_convert_to_png(remaining, auto_install=auto_install)
                    if converted:
                        log.info(f"  追加変換 (参照なし): {remaining.name} → {converted.name}")
                    else:
                        log.warning(f"  PNG 変換不可 (参照なし): {remaining.name}")
        else:
            log.warning(
                f"短縮形プレースホルダーが {truncated_count} 件ありますが、"
                "元の docx ファイルが不明なため抽出できません。"
                "--original オプションで元ファイルを指定してください。"
            )

    # ── xlsx 埋め込み画像の抽出（プレースホルダーなし → Markdown 末尾に追記）──
    if original_path and original_path.suffix.lower() in (".xlsx", ".xlsm"):
        xlsx_images = _extract_xlsx_media(original_path, images_dir, auto_install=auto_install)
        if xlsx_images:
            log.info(f"xlsx 埋め込み画像 {len(xlsx_images)} 件を末尾に追記します。")
            appendix = "\n\n---\n\n## 埋め込み画像\n\n"
            for img in xlsx_images:
                rel = str(img.relative_to(md_path.parent))
                appendix += f"![{img.stem}]({rel})\n\n"
            text += appendix
            total += len(xlsx_images)

    if total == 0 and truncated_count == 0:
        log.info("埋め込み画像はありませんでした。")
    else:
        log.info(f"埋め込み画像 {total} 件を抽出・参照更新しました → {images_dir}")

    md_path.write_text(text, encoding="utf-8")
    return total


# ---------------------------------------------------------------------------
# エントリーポイント
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Office ファイルを Markdown に変換します",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", help="変換対象のファイルパス")
    parser.add_argument(
        "-o", "--output",
        help="出力 Markdown ファイルのパス（省略時: 入力ファイル名.md）",
    )
    parser.add_argument(
        "--mode", choices=["a", "b", "c"], default="a",
        help="処理方針 a=テキストのみ(デフォルト) b=LLMビジョン c=PNG抽出",
    )
    parser.add_argument(
        "--images-dir", default="assets/images",
        help="方針Cで画像を保存するディレクトリ（デフォルト: assets/images）",
    )
    parser.add_argument(
        "--llm-model", default="gpt-4o",
        help="方針Bで使用する LLM モデル（デフォルト: gpt-4o）",
    )
    parser.add_argument(
        "--extract-images", action="store_true",
        help="変換後に Markdown 内の base64 埋め込み画像をファイルとして抽出する",
    )
    parser.add_argument(
        "--auto-install", action="store_true",
        help="PNG 変換に必要な ImageMagick が未インストールの場合、自動でインストールする",
    )
    args = parser.parse_args()

    # --extract-images 使用時、元ファイルパスは input と同じ（短縮形の ZIP 抽出に使う）


    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"ファイルが見つかりません: {input_path}")
        sys.exit(1)

    if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        log.error(
            f"未対応の形式です: {input_path.suffix}\n"
            f"対応形式: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )
        sys.exit(1)

    output_path = Path(args.output) if args.output else input_path.with_suffix(".md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    _images_dir_raw = Path(args.images_dir)
    images_dir = _images_dir_raw.parent / _images_dir_raw.name.replace(" ", "_")

    log.info(f"変換開始: {input_path} → {output_path} (方針{args.mode.upper()})")

    try:
        if args.mode == "a":
            convert_mode_a(input_path, output_path)
        elif args.mode == "b":
            convert_mode_b(input_path, output_path, args.llm_model)
        elif args.mode == "c":
            convert_mode_c(input_path, output_path, images_dir)

        if args.extract_images:
            extract_embedded_images(
                output_path, images_dir,
                original_path=input_path,
                auto_install=args.auto_install,
            )
    except RuntimeError as e:
        log.error(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

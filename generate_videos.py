#!/usr/bin/env python3
"""Haftalik kisa ozet videolari uretir (slayt + Turkce sesli anlatim)."""

import asyncio
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import edge_tts
    from PIL import Image, ImageDraw, ImageFont
    import imageio_ffmpeg
except ImportError:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "edge-tts", "pillow", "imageio-ffmpeg", "-q"]
    )
    import edge_tts
    from PIL import Image, ImageDraw, ImageFont
    import imageio_ffmpeg

from video_data import WEEK_VIDEOS

BASE = Path(__file__).parent
OUT_DIR = BASE / "videos"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "tr-TR-AhmetNeural"
W, H = 854, 480


def load_fonts():
    candidates = [
        ("C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/segoeui.ttf"),
        ("C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf"),
    ]
    for bold, regular in candidates:
        bold_path, regular_path = Path(bold), Path(regular)
        if bold_path.exists() and regular_path.exists():
            return (
                ImageFont.truetype(str(bold_path), 38),
                ImageFont.truetype(str(regular_path), 26),
                ImageFont.truetype(str(regular_path), 20),
            )
    default = ImageFont.load_default()
    return default, default, default


FONT_TITLE, FONT_LINE, FONT_SMALL = load_fonts()


def wrap_text(text: str, font, max_width: int, draw: ImageDraw.ImageDraw):
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        if draw.textlength(test, font=font) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [text]


def render_slide(slide: dict, week_num: int, out_path: Path):
    img = Image.new("RGB", (W, H), "#f8f9fb")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 6], fill="#b91c1c")
    draw.rectangle([0, H - 4, W, H], fill="#e8ebf0")

    badge = f"Hafta {week_num}"
    draw.rounded_rectangle([36, 28, 36 + draw.textlength(badge, font=FONT_SMALL) + 24, 58], radius=8, fill="#b91c1c")
    draw.text((48, 34), badge, fill="white", font=FONT_SMALL)

    title = slide["title"]
    draw.text((36, 78), title, fill="#1a1d26", font=FONT_TITLE)

    y = 140
    for line in slide.get("lines", []):
        for wrapped in wrap_text(line, FONT_LINE, W - 72, draw):
            draw.text((48, y), f"•  {wrapped}", fill="#5c6370", font=FONT_LINE)
            y += 34
        y += 6

    draw.text((36, H - 36), "Internet Programciligi II — Ders Notu Arsivi", fill="#9ca3af", font=FONT_SMALL)
    img.save(out_path, "PNG", optimize=True)


async def synthesize(text: str, out_path: Path):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(out_path))


def media_duration(path: Path) -> float:
    proc = subprocess.run(
        [FFMPEG, "-i", str(path), "-f", "null", "-"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    match = re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", proc.stderr)
    if not match:
        return 4.0
    h, m, s = match.groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def make_segment(png: Path, audio: Path, out_mp4: Path):
    subprocess.run(
        [
            FFMPEG,
            "-y",
            "-loop",
            "1",
            "-i",
            str(png),
            "-i",
            str(audio),
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(out_mp4),
        ],
        capture_output=True,
        check=True,
    )


def concat_segments(segments: list[Path], out_mp4: Path):
    list_file = out_mp4.with_suffix(".txt")
    lines = [f"file '{seg.resolve().as_posix()}'" for seg in segments]
    list_file.write_text("\n".join(lines), encoding="utf-8")
    subprocess.run(
        [
            FFMPEG,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(list_file),
            "-c",
            "copy",
            str(out_mp4),
        ],
        capture_output=True,
        check=True,
    )
    list_file.unlink(missing_ok=True)


async def build_week_video(week: dict, tmp: Path) -> Path:
    num = week["num"]
    segments = []
    for i, slide in enumerate(week["slides"]):
        png = tmp / f"h{num}-s{i}.png"
        mp3 = tmp / f"h{num}-s{i}.mp3"
        seg = tmp / f"h{num}-s{i}.mp4"
        render_slide(slide, num, png)
        await synthesize(slide["say"], mp3)
        make_segment(png, mp3, seg)
        segments.append(seg)
        print(f"  slayt {i + 1}/{len(week['slides'])} ({media_duration(mp3):.1f}s)")

    out = OUT_DIR / f"hafta-{num}.mp4"
    concat_segments(segments, out)
    size_kb = out.stat().st_size // 1024
    print(f"  -> {out.name} ({size_kb} KB, ~{media_duration(out):.0f}s)")
    return out


async def main():
    OUT_DIR.mkdir(exist_ok=True)
    print(f"FFmpeg: {FFMPEG}")
    print(f"Cikti: {OUT_DIR}\n")

    with tempfile.TemporaryDirectory(prefix="intprog2-vid-") as tmp_dir:
        tmp = Path(tmp_dir)
        for week in WEEK_VIDEOS:
            print(f"Hafta {week['num']}: {week['title']}")
            await build_week_video(week, tmp)
            print()

    print("Tamamlandi. Siteyi guncellemek icin: py build_site.py")


if __name__ == "__main__":
    asyncio.run(main())

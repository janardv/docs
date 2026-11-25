#!/usr/bin/env python3
"""Place an Oculon app screenshot on a branded background for the docs.

House style (agreed 2026-11-25):
- Canvas: 5226 x 3252, same size as the backgrounds in images/img-bg/.
- The app window is pinned to ONE corner of the canvas (tl, tr, bl, or br),
  with 236 px of background on its left/right side and 288 px on its
  top/bottom side. It runs off the other two edges, so exactly one corner
  of the app window is visible. Never show two window corners.
- Zoom is chosen so the focus area (the highlighted region, open menu, or
  popup the page is about) is fully visible with a 150 px margin, as large
  as possible, capped at 2.0x. Pass the focus box in source-image pixels.
- Pick the corner nearest the focus area. With --corner auto the script
  picks the corner that allows the largest zoom.
- No drop shadow. The source screenshot keeps its own rounded, transparent corners.

Backgrounds rotate in order bg-1 -> bg-5. Pass --bg explicitly, or --index N
(0-based image number in the series) to pick bg (N % 5) + 1.

Usage:
    python3 frame_screenshot.py SRC.png OUT.png --bg-dir BG_DIR (--bg FILE | --index N) \\
        --focus X0 Y0 X1 Y1 [--corner auto|tl|tr|bl|br] [--scale S]
"""
import argparse
from pathlib import Path

from PIL import Image

CANVAS = (5226, 3252)
PAD_X, PAD_Y = 236, 288
MARGIN = 150
MAX_SCALE = 2.0
BG_FILES = ["bg - 1.png", "bg -2.png", "bg -3.png", "bg -4.png", "bg -5.png"]


def fit_scale(corner, focus, size):
    """Largest scale that keeps the focus box visible for this corner."""
    W, H = CANVAS
    sw, sh = size
    x0, y0, x1, y1 = focus
    avail_w = W - PAD_X - MARGIN
    avail_h = H - PAD_Y - MARGIN
    need_w = x1 if corner[1] == "l" else sw - x0
    need_h = y1 if corner[0] == "t" else sh - y0
    s = min(avail_w / max(need_w, 1), avail_h / max(need_h, 1), MAX_SCALE)
    # Window must overflow the two far edges so only one corner shows.
    s_min = max((W - PAD_X) / sw, (H - PAD_Y) / sh) + 0.01
    return s, s_min


def position(corner, s, size):
    W, H = CANVAS
    sw, sh = size
    x = PAD_X if corner[1] == "l" else W - PAD_X - round(sw * s)
    y = PAD_Y if corner[0] == "t" else H - PAD_Y - round(sh * s)
    return x, y


def main():
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("out")
    p.add_argument("--bg-dir", required=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--bg", help="background file name inside --bg-dir")
    g.add_argument("--index", type=int, help="0-based position in the series; picks bg (index %% 5) + 1")
    p.add_argument("--focus", type=int, nargs=4, metavar=("X0", "Y0", "X1", "Y1"),
                   help="focus box in source pixels; defaults to the top-left 45%% of the source")
    p.add_argument("--corner", default="auto", choices=["auto", "tl", "tr", "bl", "br"])
    p.add_argument("--scale", type=float, help="override the computed zoom")
    a = p.parse_args()

    src = Image.open(a.src).convert("RGBA")
    size = src.size
    focus = a.focus or (0, 0, int(size[0] * 0.45), int(size[1] * 0.45))

    corners = ["tl", "tr", "bl", "br"] if a.corner == "auto" else [a.corner]
    best = max(corners, key=lambda c: fit_scale(c, focus, size)[0])
    s, s_min = fit_scale(best, focus, size)
    if a.scale:
        s = a.scale
    if s < s_min:
        print(f"warning: scale {s:.3f} < {s_min:.3f}; raising it so only one corner shows "
              f"(focus box may be clipped)")
        s = s_min

    bg_name = a.bg if a.bg else BG_FILES[a.index % len(BG_FILES)]
    bg = Image.open(Path(a.bg_dir) / bg_name).convert("RGBA")
    if bg.size != CANVAS:
        bg = bg.resize(CANVAS, Image.LANCZOS)

    win = src.resize((round(size[0] * s), round(size[1] * s)), Image.LANCZOS)
    x, y = position(best, s, size)
    canvas = bg.copy()
    # Crop the part of the window that lands on the canvas, then composite it.
    cx0, cy0 = max(0, -x), max(0, -y)
    cx1 = min(win.width, CANVAS[0] - x)
    cy1 = min(win.height, CANVAS[1] - y)
    canvas.alpha_composite(win.crop((cx0, cy0, cx1, cy1)), (max(x, 0), max(y, 0)))
    canvas.convert("RGB").save(a.out, optimize=True)
    print(f"{a.out}  bg={bg_name}  corner={best}  scale={s:.3f}")


if __name__ == "__main__":
    main()

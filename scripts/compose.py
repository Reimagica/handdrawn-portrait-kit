"""Place transparent PNG modules on a canvas using a JSON layout."""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageColor


def compose(layout_path: Path, output_path: Path) -> None:
    if output_path.suffix.lower() != ".png":
        raise ValueError("Output filename must end in .png")
    if output_path.exists():
        raise ValueError(f"Output already exists: {output_path}")

    layout = json.loads(layout_path.read_text(encoding="utf-8-sig"))
    canvas_width, canvas_height = layout["canvas"]
    if not all(type(size) is int and size > 0 for size in (canvas_width, canvas_height)):
        raise ValueError("Canvas width and height must be positive integers")

    background = layout.get("background", "#fcf8f4")
    color = (0, 0, 0, 0) if background is None else ImageColor.getcolor(background, "RGBA")
    canvas = Image.new("RGBA", (canvas_width, canvas_height), color)

    layers = layout["layers"]
    if not layers:
        raise ValueError("Layout needs at least one layer")
    has_decoration = any(layer.get("role") == "decoration" for layer in layers)
    portrait_top_limit = layout.get("portrait_top_limit", 16 if has_decoration else 12)
    if type(portrait_top_limit) is not int or not 0 <= portrait_top_limit <= 100:
        raise ValueError("portrait_top_limit must be an integer percentage from 0 to 100")
    for layer in layers:
        asset_path = layout_path.parent / layer["file"]
        x = layer["x"]
        if ("width" in layer) == ("height" in layer):
            raise ValueError(f"Specify exactly one of width or height: {asset_path}")
        size = layer["width"] if "width" in layer else layer["height"]
        if type(x) is not int or type(size) is not int or size <= 0:
            raise ValueError(f"Expected integer x and positive integer width or height: {asset_path}")

        with Image.open(asset_path) as source:
            asset = source.convert("RGBA")
        if "crop" in layer:
            left, top, right, bottom = layer["crop"]
            if (
                any(type(value) is not int for value in (left, top, right, bottom))
                or not (0 <= left < right <= asset.width and 0 <= top < bottom <= asset.height)
            ):
                raise ValueError(f"Crop must be an integer rectangle within the source PNG: {asset_path}")
            asset = asset.crop((left, top, right, bottom))
        bounds = asset.getchannel("A").getbbox()
        if bounds is None:
            raise ValueError(f"Layer has no visible pixels: {asset_path}")
        asset = asset.crop(bounds)
        if "width" in layer:
            width, height = size, max(1, round(asset.height * size / asset.width))
        else:
            width, height = max(1, round(asset.width * size / asset.height)), size
        if ("bottom" in layer) == ("y" in layer):
            raise ValueError(f"Specify exactly one of y or bottom: {asset_path}")
        position = layer["bottom"] if "bottom" in layer else layer["y"]
        if type(position) is not int:
            raise ValueError(f"Expected integer y or bottom: {asset_path}")
        y = canvas_height - height - position if "bottom" in layer else position
        role = layer.get("role")
        clip_sides = layer.get("clip_sides", [])
        if not isinstance(clip_sides, list) or any(side not in ("left", "right") for side in clip_sides):
            raise ValueError(f"clip_sides must list left and/or right: {asset_path}")
        if clip_sides and role not in ("portrait", "landscape"):
            raise ValueError(f"Only portraits and landscapes can specify clip_sides: {asset_path}")
        if (
            (x < 0 and "left" not in clip_sides)
            or (x + width > canvas_width and "right" not in clip_sides)
            or y < 0
            or y + height > canvas_height
            or x >= canvas_width
            or x + width <= 0
        ):
            raise ValueError(f"Layer would be clipped at ({x}, {y}), {width}×{height}: {asset_path}")
        if (asset.width, asset.height) != (width, height):
            asset = asset.resize((width, height), Image.Resampling.LANCZOS)
        if x < 0 or x + width > canvas_width:
            asset = asset.crop((max(0, -x), 0, min(width, canvas_width - x), height))
            x = max(0, x)
        if role in ("portrait", "landscape"):
            visible = asset.getchannel("A").getbbox()
            if visible is None:
                raise ValueError(f"Layer has no visible pixels inside the canvas: {asset_path}")
            top, bottom = y + visible[1], y + visible[3]
            if canvas_height - bottom > round(0.03 * canvas_height):
                raise ValueError(f"The {role} must be within 3% of the bottom edge: {asset_path}")
            if role == "portrait" and top > round(portrait_top_limit * canvas_height / 100):
                raise ValueError(f"Portrait top margin exceeds {portrait_top_limit}%. Enlarge its core or use a shorter canvas: {asset_path}")
            if role == "landscape":
                landscape_height = bottom - top
                minimum_height = round(0.45 * canvas_height)
                if landscape_height < minimum_height:
                    raise ValueError(f"The landscape must cover at least 45% of the canvas height: {asset_path}")
                if has_decoration:
                    maximum_height = round(0.55 * canvas_height)
                    if not (minimum_height <= top <= maximum_height and landscape_height <= maximum_height):
                        raise ValueError(f"With decorations, the landscape must occupy about the lower half: {asset_path}")
        canvas.alpha_composite(asset, (x, y))

    with output_path.open("xb") as output:
        canvas.save(output, format="PNG", dpi=(300, 300))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("layout", type=Path, help="JSON layout file")
    parser.add_argument("output", type=Path, help="New PNG output path")
    args = parser.parse_args()
    try:
        compose(args.layout, args.output)
    except (KeyError, OSError, TypeError, ValueError) as exc:
        parser.exit(1, f"Unable to compose: {exc}\n")


if __name__ == "__main__":
    main()

import json
from pathlib import Path

pywalpath = Path.home() / ".cache" / "wal" / "colors.json"

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

with open(pywalpath) as f:
    wal = json.load(f)

colors = wal["colors"]
special = wal["special"]

theme = {
    "manifest_version": 3,
    "name": "pychrome",
    "version": "1.0",
    "description": "chromium theme with pywal cuz i wanna match my current setup ay",
    "theme": {
        "colors": {
            "frame": hex_to_rgb(special["background"]),
            "frame_inactive": hex_to_rgb(colors["color0"]),
            "toolbar": hex_to_rgb(colors["color8"]),
            "tab_background_text": hex_to_rgb(special["foreground"]),
            "tab_text": hex_to_rgb(special["foreground"]),
            "bookmark_text": hex_to_rgb(special["foreground"]),
            "button_background": hex_to_rgb(colors["color8"]),
            "ntp_background": hex_to_rgb(special["background"]),
            "ntp_text": hex_to_rgb(special["foreground"]),
            "ntp_link": hex_to_rgb(colors["color4"])
        }
    }
}

with open("manifest.json", "w") as f:
    json.dump(theme, f, indent=4)

print("applied theme!")
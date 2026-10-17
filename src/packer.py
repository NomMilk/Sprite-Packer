from PIL import Image
import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    base_path = Path(sys.executable).parent
else:
    base_path = Path(__file__).resolve().parent

input_folder = base_path / "PngFiles"

files = [f for f in os.listdir(input_folder) if f.lower().endswith(".png")]
files.sort()

images = [Image.open(os.path.join(input_folder, f)) for f in files]

if not images:
    raise ValueError("No PNG images found in the folder.")

max_width = max(img.width for img in images)
max_height = max(img.height for img in images)

spacing = max(max_width, max_height)

output_path = base_path / (str(max_width) + ' ' + str(max_height) + ".png") 

total_width = len(images) * spacing
total_height = max_height

canvas = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 0))

for i, img in enumerate(images):
    x = i * spacing
    y = (max_height - img.height) // 2  # vertically center
    canvas.paste(img, (x, y), img if img.mode == "RGBA" else None)

# Save result
canvas.save(output_path)

print(f"Saved combined image to {output_path}")

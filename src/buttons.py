from customtkinter import *
from PIL import Image
import os
import sys
from pathlib import Path

class Buttons(CTkFrame):
	def __init__(self, master, **kwargs):
		FontManager.load_font("assets/ComicRelief-Regular.ttf")

		super().__init__(master, **kwargs)
		self.configure(bg_color = "#1A2129")
		self.configure(fg_color = "#1A2129")
		self.configure(corner_radius = 0)

		self.button_pack = CTkButton(
			master=self,
			text=" Pack ",
			font=("Tiny5", 50),
			corner_radius=0,
			fg_color="#312137",
			text_color="#713141",
			hover_color = "#1A2129",
			command=self.pack_sprites
		)

		self.button_pack.grid(row=0, column=0, padx=0)

	def pack_sprites(self):
		filenames = filedialog.askopenfilenames(initialdir = "D:/Downloads",
						  title = "Select Files",
						  filetypes = [("Png files", "*.png")])
		print(filenames)
		files = [f for f in filenames]
		files.sort()

		images = [Image.open(f) for f in files]

		if not images:
		    raise ValueError("No PNG images found in the folder.")

		self.button_pack.configure(text="Loading...")

		max_width = max(img.width for img in images)
		max_height = max(img.height for img in images)

		spacing_width = max_width
		spacing_height = max_height

		general_path = filedialog.askdirectory()
		output_path = general_path + ('/' + str(max_width) + ' ' + str(max_height) + ".png")

		total_width = len(images) * spacing_width
		total_height = max_height

		canvas = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 0))

		for i, img in enumerate(images):
		    x = i * spacing
		    y = (max_height - img.height) // 2  # vertically center
		    canvas.paste(img, (x, y), img if img.mode == "RGBA" else None)

		canvas.save(output_path)
		self.master.destroy()

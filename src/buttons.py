from customtkinter import *
from PIL import Image
import os
import sys
import math
from pathlib import Path

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join(base_path, relative_path)


class Buttons(CTkFrame):
	def __init__(self, master, **kwargs):
		FontManager.load_font(resource_path("assets/ComicRelief-Regular.ttf"))

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
		
		spacing_width = max(img.width for img in images)
		spacing_height = max(img.height for img in images)

		general_path = filedialog.askdirectory()
		output_path = general_path + ('/' + str(spacing_width) + ' ' + str(spacing_height) + ".png")

		amtOfX = 1
		amtOfY = len(images)

		total_width = amtOfX * spacing_width
		total_height = amtOfY * spacing_height 
		
		while total_height > total_width:
			amtOfX += 1
			amtOfY = math.ceil(len(images) / amtOfX)

			total_width = amtOfX * spacing_width
			total_height = amtOfY * spacing_height 
		
		print(amtOfX, amtOfY)

		canvas = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 0))

		for I in range(amtOfX):
			x = I * spacing_width
			for II in range(amtOfY):
				print(I + II * amtOfX)
				if (I + II * amtOfX) > len(images) - 1:
					continue
				img = images[I + II * amtOfX]
				y = (II * spacing_height) + (spacing_height - img.height) // 2
				canvas.paste(img, (x, y), img if img.mode == "RGBA" else None)

		canvas.save(output_path)
		self.master.destroy()

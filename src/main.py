from customtkinter import *
import PIL
from PIL import Image
from buttons import Buttons

class Packer(CTk):
	def __init__(self):
		super().__init__()

		FontManager.load_font("assets/Tiny5-Regular.ttf")

		image = PIL.Image.open("assets/stolen_background.png")
		background_image = CTkImage(image, size=(600, 600))


		self.title("Fish's Sprite Packer")
		self.geometry("600x600")
		self.resizable(False, False)

		bg_lbl = CTkLabel(self, text="", image=background_image)
		bg_lbl.place(x=0, y=0)

		self.grid_columnconfigure(0, weight=1)

		self.title_label = CTkLabel(
			master=self,
			text="Sprite Packer",
			bg_color = "#1A2129",
			text_color = "#713141",
			font=("Tiny5", 30)
		)
		self.title_label.grid(row=0, column=0, padx=(0, 350), pady=10)

		self.button_area = Buttons(master=self)
		self.button_area.grid(row=1, column=0, padx=(0, 0), pady=(200, 0))

if __name__ == "__main__":
	app = Packer()
	app.mainloop()

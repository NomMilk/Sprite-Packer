from customtkinter import *
from buttons import Buttons

class Packer(CTk):
	def __init__(self):
		super().__init__()

		FontManager.load_font("assets/ComicRelief-Regular.ttf")

		self.title("Fish's Sprite Packer")
		self.geometry("600x600")
		self.resizable(False, False)

		self.grid_columnconfigure(0, weight=1)

		self.title_label = CTkLabel(
			master=self,
			text="Sprite Packer",
			font=("Comic Relief", 30)
		)
		self.title_label.grid(row=0, column=0, padx=10, pady=10)

		self.button_area = Buttons(master=self)
		self.button_area.grid(row=1, column=0, pady=10)

if __name__ == "__main__":
	app = Packer()
	app.mainloop()

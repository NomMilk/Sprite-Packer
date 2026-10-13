from customtkinter import *

class Buttons(CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.pack = CTkButton(master=self, text="Pack", command=self.pack_sprites)
		self.pack.grid(row=0, column=0, padx=0)

		self.margin_x = CTkLabel(
			master=self,
			text="X - Margin: 100",
			font=("Arial", 30)
		)

		self.margin_x.grid(row=1, column=0, padx=0)

		self.margin_y = CTkLabel(
			master=self,
			text="Y - Margin: 100",
			font=("Arial", 30)
		)

		self.margin_y.grid(row=2, column=0, padx=0)

	def pack_sprites(_):
		print("hi")

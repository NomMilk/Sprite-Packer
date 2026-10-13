from customtkinter import *

class Buttons(CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.CTkButton = customtkinter.CTkLabel(master=self, text="Pack", command=pack_sprites)

	def pack_sprites():
		print("hi")

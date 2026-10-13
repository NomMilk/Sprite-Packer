from customtkinter import *

class Packer(CTk):
	def __init__(self):
		super().__init__()

		self.title("Fish's Sprite Packer")
		self.geometry("600x600")
		self.resizable(False, False)

		self.grid_columnconfigure(0, weight=1)

		self.title_label = CTkLabel(
			master=self,
			text="Sprite Packer",
			font=("Arial", 30)
		)
		self.title_label.grid(row=30, column=0, pady=(20, 0))

if __name__ == "__main__":
	app = Packer()
	app.mainloop()

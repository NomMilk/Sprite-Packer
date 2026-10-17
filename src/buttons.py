from customtkinter import *

class Buttons(CTkFrame):
	def __init__(self, master, **kwargs):
		FontManager.load_font("assets/ComicRelief-Regular.ttf")

		super().__init__(master, **kwargs)
		self.configure(bg_color = "#1A2129")
		self.configure(fg_color = "#1A2129")
		self.configure(corner_radius = 0)

		self.button_pack = CTkButton(
			master=self,
			text="Pack",
			font=("Tiny5", 30),
			corner_radius=0,
			fg_color="#312137",
			text_color="#713141",
			hover_color = "#1A2129",
			command=self.pack_sprites
		)

		self.button_pack.grid(row=0, column=0, padx=0)

		self.margin_x = CTkLabel(
			master=self,
			text="X: ##",
			corner_radius=0,
			font=("Tiny5", 30),
			bg_color="#1A2129",
			text_color = "#713141"
		)

		self.margin_x.grid(row=1, column=0, padx=0)

		self.margin_y = CTkLabel(
			master=self,
			text="Y: ##",
			corner_radius=0,
			font=("Tiny5", 30),
			bg_color="#1A2129",
			text_color = "#713141"
		)

		self.margin_y.grid(row=2, column=0, padx=0)

	def pack_sprites(_):
		filenames = filedialog.askopenfilenames(initialdir = "/",
						  title = "Select Files",
						  filetypes = [("Png files", "*.png")])
		print(filenames)

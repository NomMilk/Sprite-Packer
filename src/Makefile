build-linux:
	pyinstaller --onefile --add-data="./assets:assets" --noconsole --hidden-import=PIL._tkinter_finder --hidden-import=PIL.ImageTk main.py --distpath ../dist/

build-window:
	pyinstaller --onefile --add-data="./assets:assets" --name="Sprite Packer" --icon="./assets/Fish.ico" --noconsole --hidden-import=PIL._tkinter_finder --hidden-import=PIL.ImageTk main.py --distpath ../dist/


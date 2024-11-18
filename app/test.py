from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk

path = filedialog.asksaveasfilename(
    title="Save file as",
    defaultextension=".png",
    filetypes=[
        ("Image PNG", "*.png"),
        ("Image JPG", "*.jpg *.jpeg"),
        ("All files", "*.*")
    ],
    initialfile="web-dev.png"
)

print(path)

input_path = "./img/web-dev.jpg"
output_path = path + "web-dev.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path, format="PNG")
Image.open(output_path)
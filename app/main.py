from rembg import remove
from tkinter import filedialog
from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

##! CONSTANST
SCREEN_SIZE      = '600x400'
COLOR_BACKGROUND = 'white'

##! LOGIC

def extract_path(path):
    split_path = path.split("/")
    output_path = split_path[-1]
    if output_path.find(".jpg") != -1:
        output_path = output_path.replace(".jpg", ".png")
    elif output_path.find(".jpeg") != -1:
        output_path = output_path.replace(".jpeg", ".png")

    return output_path
    
def drop(event):
    image_path = event.data
    print("Upload image successful", image_path)
    image_path = extract_path(image_path)
    convert_to_png(image_path)

def convert_to_png(image):
    try:
        input_path = image
        output_path = extract_path(input_path)
        inp = Image.open(input_path)
        output = remove(inp)
        output.save(output_path)
        Image.open(output_path)
    except:
        print("There was a problem")

def selected_image():
    path_image = filedialog.askopenfilename(
        title="Selected image",
        filetypes=[("Files of images", "*.png *.jpg *.jpeg *.gif")]
    )
    if path_image.split("/")[-1].find(".png") != -1:
        print("The picture is a picture in format png")
    else:
        print("Image selected: ", path_image)
        convert_to_png(path_image)


# Initialize the app
app = TkinterDnD.Tk()

# Set the windows
app.geometry(SCREEN_SIZE)
app.title("Convert to png")
app.configure(bg=COLOR_BACKGROUND)

########################! CENTER FRAME ##############################
main_frame = Frame(app, width=600, height=300, bd=2, relief='groove')
main_frame.pack(expand=True)
main_frame.pack_propagate(False)

#! ##################################################################

#######################! BUTTON DOWN ################################
selected_button = Button(app, text="Selected image", width=20, height=2, command=selected_image)
selected_button.pack(side=BOTTOM, pady=10)

#! ##################################################################

# Set icon drop
icon_image = Image.open("./img/drag-and-drop.png").convert("RGBA")
icon_image = icon_image.resize((200, 200))
alpha = 32  # Ajusta este valor para cambiar la opacidad (128 para 50% de transparencia)
icon_data = icon_image.getdata()
icon_image = Image.new("RGBA", icon_image.size)
icon_image.putdata([(r, g, b, alpha) for r, g, b, a in icon_data])
icon_tk = ImageTk.PhotoImage(icon_image)

icon_label = Label(main_frame, image=icon_tk, bg=COLOR_BACKGROUND)
icon_label.pack(pady=20)

message_label = Label(main_frame, text="Drop the image you want", font=("Arial", 12), fg="#666666")
message_label.pack()

###################! EVENTS ########################################
app.drop_target_register(DND_FILES)
app.dnd_bind("<<Drop>>", drop)

# Loop to start the app
app.mainloop()

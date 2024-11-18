from rembg import remove
from tkinter import filedialog
from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

# Initialize the app
app = TkinterDnD.Tk()

##! CONSTANST
SCREEN_SIZE      = f'600x400+{round((app.winfo_screenwidth()/2) - 250)}+{round((app.winfo_screenheight()/2) - 250)}'#600x400
MODAL_SIZE       = f'300x200+{round((app.winfo_screenwidth()/2) -100)}+{round((app.winfo_screenheight()/2) - 150)}'
COLOR_BACKGROUND = 'white'

##! LOGIC

#! #################### MODALS #####################################
def modal_confim():
    # Created a modal window
    modal_window = Toplevel(app)
    modal_window.title("Successful")
    modal_window.geometry(MODAL_SIZE)
    modal_window.transient(app)
    # Block the main window
    modal_window.grab_set()

    #! ############# LABEL ####################
    label = Label(modal_window, 
                  text="The image upload successfuly", 
                  font=("Arial", 16), 
                  fg="#00F226",
                  wraplength=280)
    label.pack(pady=60)
    #! ########################################

    modal_window.bind("<Escape>", lambda event: modal_window.destroy())

    app.wait_window(modal_window)

def modal_success():
    # Created a modal window
    modal_window = Toplevel(app)
    modal_window.title("Successful")
    modal_window.geometry(MODAL_SIZE)
    modal_window.transient(app)
    # Block the main window
    modal_window.grab_set()

    #! ############# LABEL ####################
    label = Label(modal_window, 
                  text="The image has been " +
                  "transformed to png",
                  font=("Arial", 16),
                  fg="#00F226",
                  wraplength=280)
    label.pack(pady=60)
    #! ########################################

    modal_window.bind("<Escape>", lambda event: modal_window.destroy())

    app.wait_window(modal_window)

def modal_fail():
    # Created a modal window
    modal_window = Toplevel(app)
    modal_window.title("Failure")
    modal_window.geometry(MODAL_SIZE)
    modal_window.transient(app)
    # Block the main window
    modal_window.grab_set()

    #! ############# LABEL ####################
    label = Label(modal_window, 
                  text="There was a problem, it couldn't transform to png",
                  font=("Arial", 16),
                  fg="#FC0808",
                  wraplength=280)
    label.pack(pady=60)
    #! ########################################

    modal_window.bind("<Escape>", lambda event: modal_window.destroy())

    app.wait_window(modal_window)

def modal_same_png():
    # Created a modal window
    modal_window = Toplevel(app)
    modal_window.title("PNG format")
    modal_window.geometry(MODAL_SIZE)
    modal_window.transient(app)
    # Block the main window
    modal_window.grab_set()

    #! ############# LABEL ####################
    label = Label(modal_window,
                  text="The picture is a picture in format png", 
                  font=("Arial", 16),
                  wraplength=280)
    label.pack(pady=60)
    #! ########################################

    modal_window.bind("<Escape>", lambda event: modal_window.destroy())

    app.wait_window(modal_window)

def modal_save(image):
    # Created a modal window
    modal_window = Toplevel(app)
    modal_window.title("Save image")
    modal_window.geometry(MODAL_SIZE)
    modal_window.transient(app)
    # Block the main window
    modal_window.grab_set()

    preview_image, filename = convert_to_png(image)
    preview_size_image = preview_image.resize((200, 100))
    preview_tkimage = ImageTk.PhotoImage(preview_size_image)

    #! ############# FRAME ####################
    frame = Frame(modal_window, width=300, height=100, bd=1, relief="groove")
    frame.pack(expand=True)
    frame.pack_propagate(False)
    #! ########################################

    #! ############# LABEL ####################
    preview_label = Label(frame, image=preview_tkimage)
    preview_label.pack(pady=0)

    label = Label(modal_window,
                  text="Would you like to save the image?", 
                  font=("Arial", 14),
                  wraplength=280)
    label.pack(pady=5)
    #! ########################################

    #! ############# BUTTONS ##################
    button_save = Button(modal_window,
                    text="save",
                    bg="#00F226",
                    command=lambda: save_image(preview_image, filename, modal_window))
    button_save.pack(side=LEFT, padx=60, pady=5)

    button_canceled = Button(modal_window,
                             text="canceled",
                             bg="#FC0808",
                             command=modal_window.destroy)
    button_canceled.pack(side=RIGHT, padx=40, pady=5)
    #! ########################################

    modal_window.bind("<Escape>", lambda event: modal_window.destroy())

    app.wait_window(modal_window)

#! #################################################################

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
    modal_confim()
    # convert_to_png(image_path)
    modal_save(image_path)
    modal_success()

def convert_to_png(image):
    try:
        input_path = image
        output_path = extract_path(input_path)
        inp = Image.open(input_path)
        output = remove(inp)
        return output, output_path
    except:
        modal_fail()

def save_image(output, filename, modal):
    output_path = filedialog.asksaveasfilename(
        title="Save file as",
        defaultextension=".png",
        filetypes=[
            ("Image PNG", "*.png"),
            ("Image JPG", "*.jpg *.jpeg"),
            ("All files", "*.*")
        ],
        initialfile=filename
    )
    # Verified if the file was selected
    if output_path:
        output.save(output_path)
        # Image.open(output_path)
        modal.destroy()
        modal_success()
        output.show()
    else:
        modal_fail()

def selected_image():
    path_image = filedialog.askopenfilename(
        title="Selected image",
        filetypes=[("Files of images", "*.png *.jpg *.jpeg *.gif")]
    )
    if path_image.split("/")[-1].find(".png") != -1:
        modal_same_png()
    else:
        print("Image selected: ", path_image)
        modal_confim()
        # convert_to_png(path_image)
        modal_save(path_image)

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
img1 = Image.open("./img/drag-and-drop.png")
img2 = Image.open("./img/background.png").resize(img1.size)
img2 = Image.blend(img2, img2, 0.5)
mask = Image.new("L", img1.size, 128)
icon_image = Image.composite(img2, img1, mask)
icon_image = icon_image.resize((200, 200))
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
# def main():
#     app.mainloop()

# if __name__ == "__main__":
#     main()
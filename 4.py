from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk

root = Tk()
root.geometry('800x700')
root.maxsize(800, 700)
root.minsize(576, 576)

# inserting the image using PIL ->  first we have to use Image.open(filename)
# to open the image in a variable an then we have to read the image as Imagetk.PhotoImage(varnmae)
pic = Image.open("2.png")  # reading the jpg fi le
img = ImageTk.PhotoImage(pic)  # giving the read image to show on the scree, it will read jpg files too
# pic.show()

'''
txt = Label(text="sbka photo aage background me okk ")
txt.pack()
# inserting image on the window --> it supports only png file format
photo = PhotoImage(file="1.png")  # importing the image into a variable using PhotoImage method
img_lab = Label(image=photo)  # creating the label for the image
img_lab.pack()  # packing the image label so that it can appear on the screen

'''

# to make it read all type of file we have to use pillow library , PIL(python image library),
# install it, its modules allows us to use jpg file formats
root.mainloop()

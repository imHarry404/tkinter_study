from tkinter import *
from PIL import Image, ImageTk

harry_root = Tk()  # this creates a basic GUI, basic components, its like a base for our GUI

# it takes parameter as (width x height )
harry_root.geometry('500x300')
pic = Image.open('/home/hariom/Desktop/march target/harry_tkinter/praticals/2.jpg')  # reading the jpg file
# giving the read image to show on the scree, it will read jpg files too
img = ImageTk.PhotoImage(pic)


# to fix the size of window
# width , height
# it will not allow us to resize the window against its parameter
harry_root.minsize(400, 300)
harry_root.maxsize(800, 500)  # maximum width

# in tkinter to keep something for later, we have to make label and then we have to pack it. then after it will appear on the console
hk = Label(text="This is harry's GUI")
hk.pack()  # this will cause it to appear on the console

harry_root.mainloop()  # this is the window loop , it will keep us inside the window

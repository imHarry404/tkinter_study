from tkinter import *

root = Tk()


# ctrl+alt+l to format the document

# setting up the geometry, window size, minsize, maxsize

# geometry('width x height')
root.geometry('500x400')

# minsize(width , height)
root.minsize(250, 200)

# minsize(width , height)
root.maxsize(700, 600)

harry = Label(text="This is harry")
harry.pack()
root.mainloop()

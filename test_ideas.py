from tkinter import *

root = Tk()
root.title("lorem ipsium")
root.minsize(200, 200)
root.maxsize(1080, 1080)
frame1=Frame(root, bg="white", relief=SUNKEN)
frame1.pack(side=TOP, fill=X, borderwidth=5)
label1 = Label(frame1, text="lorem ipsium")
label1.pack(side=TOP, fill=X)

root.mainloop()

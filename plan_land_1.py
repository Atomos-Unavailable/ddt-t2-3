from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
root2eng = Tk()
root2eng.destroy()
#creating a function that replaces the first gui with the second
def open_window2eng(root):
    #killing the first
    root.destroy()
    #creating the second
    root2eng = Tk()
    root2eng.title("hello")
    root2eng.minsize(200,200)
    root2eng.maxsize(1080, 1080)
    #creating a notisable filler command to see if buttons work
    def filler_command(root2eng):
        hi = Frame(root2eng, bg="grey", relief=SUNKEN)
        hi.pack(side=TOP, fill=X)
        hi_l = Label(hi, text="it works")
        hi_l.pack(side=TOP, fill=X)
    #testing the frames work right on this window
    eng_main_title = Frame(root2eng, bg="grey", relief=SUNKEN, borderwidth=5)
    eng_main_title.pack(side=TOP, fill=X)
    eng_main_title_l = Label(eng_main_title, text="Welcome to the Mac-Change Map", wraplength=200, font="TkDefaultFont")
    eng_main_title_l.pack(side=TOP, fill=X)
    #creating a frame for the textbox and button to go on
    room_frame = Frame(root2eng, bg="grey", relief=SUNKEN, borderwidth=5)
    room_frame.pack(side=TOP, fill=X)
    room_frame_label = Label(room_frame,text="lorem ipsuim", bg="grey", relief=SUNKEN, borderwidth=5)
    room_frame_label.pack(side=TOP, fill=X)
    room_code_label = ttk.Label(room_frame, text="Please enter the room code (the 2-3 character code of the 'room number') in the box below")
    room_code_label.pack(side=TOP, fill=X)
    room_code = StringVar()
    room_code_entry = ttk.Entry(room_frame, textvariable=room_code)
    room_code_entry.pack(side=TOP, fill=X)
    room_code_entry.focus()
    #creating button
    enter_button = Button(room_frame, bg="grey", relief=SUNKEN, borderwidth=5, text="Proceed to search", command =lambda: filler_command(root2eng))
    enter_button.pack(side=BOTTOM, fill=X)
    #creating a description frame at the bottom to explain the pourpose of this appliacation
    eng_main_desc = Frame(root2eng, bg="grey", relief=SUNKEN, borderwidth=5)
    eng_main_desc.pack(side=TOP, fill=X)
    eng_main_desc_l = Label(eng_main_desc, text="Our goal is to help people who aren't good with maps, people who do not speak english fluently, and just anyone in need of it. Here at Macleans we like to help people, so this is to help you find your way around the school if you are lost, or to find a location you have never been to before. Infact, we will also give you backstory about the general location, and point out wht sorts of activities take place in that area.", wraplength=375, font="TkDefaultFont")
    eng_main_desc_l.pack(side=TOP, fill=X)  
    
    #ensuring the second gui window doesn't immediately dissapear
    root2eng.mainloop()
#creating the main root for everything to go on
root = Tk()
root.title("First edition of landing page")
#creating adjustable size/scalling
root.minsize(200, 200)
root.maxsize(1080, 1080)
#creating the first frame / Title frame
title = Frame(root, bg="black", relief = SUNKEN, borderwidth = 5)
#packing frame
title.pack(side=TOP, fill=X)
#creating the first label/the text on the first frame
title_Label = Label(title, bg="grey", text="Welcome to the first edition of the Mac-Change maps GUI design!", wraplength=225)
#packing label
title_Label.pack(side=TOP, fill=X)
#creatng a frame for the main map immage
image_f =  Frame(root, bg="white", relief=SUNKEN, borderwidth = 2)
#packing it into the 2nd slot from the top
image_f.pack(side=TOP, fill=X)
#creating language box frame
language_f = Frame(root, bg="light blue", relief = SUNKEN, borderwidth = 5)
#packing frame in the bottom so that it remains at the lower poin reguardless of the adjustments of size by the user
language_f.pack(side=BOTTOM, fill=X)
#creating a label for the laguage frame to direct the user.
language_L = Label(language_f, bg="light blue", text="Pick a language option", wraplength = 175)
#packing label
language_L.pack(side=TOP, fill=X)
#creating initial box for language selection
languages = StringVar()
language_Box = ttk.Combobox(language_f, textvariable=languages)
language_Box['values'] = ['English (simplified)', 'English (Traditional)', 'Chinese (simplified)', 'Chinese (traditional)', 'French', 'Japanese', 'Thai', 'German', 'Spanish', 'Italian']
#packing the dropdown box
language_Box.pack(side=TOP, fill=X)
proceed_b = Button(language_f, bg="white", relief=SUNKEN, text="Proceed?", command=lambda:open_window2eng(root))
proceed_b.pack(side=BOTTOM, fill=X)
#ensuring the GUI stays running rather than dissapearing after it loads or remaining until the root is replaced with a different one
root.mainloop()
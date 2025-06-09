from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

root2eng = Tk()
root2eng.title("hello")
root2eng.minsize(200,200)
root2eng.maxsize(1080, 1080)
def filler_command(root2eng):
        hi = Frame(root2eng, bg="grey", relief=SUNKEN)
        hi.pack(side=TOP, fill=X)
        hi_l = Label(hi, text="it works")
        hi_l.pack(side=TOP, fill=X)
eng_main_title = Frame(root2eng, bg="navy", relief=SUNKEN, borderwidth=5)
eng_main_title.pack(side=TOP, fill=X)
eng_main_title_l = Label(eng_main_title, text="Welcome to the Mac-Change Map", wraplength=200, font="TkDefaultFont")
eng_main_title_l.pack(side=TOP, fill=X)

room_frame = Frame(root2eng, bg="grey", relief=SUNKEN, borderwidth=5)
room_frame.pack(side=TOP, fill=X)
room_frame_label = Label(room_frame,text="lorem ipsuim", bg="grey", relief=SUNKEN, borderwidth=5)
room_frame_label.pack(side=TOP, fill=X)
room_code_label = ttk.Label(room_frame, text="Please enter the room code (the 2-3 character code of the 'room number') in the box below")
room_code_label.pack(side=TOP, fill=X)

room_code = StringVar()
room_code_entry = ttk.Entry(room_frame, textvariable=room_code)
room_code_entry.pack(side=TOP, fill=X)

enter_button = Button(room_frame, bg="grey", relief=SUNKEN, borderwidth=5, text="Proceed to search", command =lambda: filler_command(root2eng))
enter_button.pack(side=BOTTOM, fill=X)

eng_main_desc = Frame(root2eng, bg="light blue", relief=SUNKEN, borderwidth=5)
eng_main_desc.pack(side=TOP, fill=X)
eng_main_desc_l = Label(eng_main_desc, text="Our goal is to help people who aren't good with maps, people who do not speak english fluently, and just anyone in need of it. Here at Macleans we like to help people, so this is to help you find your way around the school if you are lost, or to find a location you have never been to before. Infact, we will also give you backstory about the general location, and point out wht sorts of activities take place in that area.", wraplength=375, font="TkDefaultFont")
eng_main_desc_l.pack(side=TOP, fill=X)  

root2eng.mainloop()
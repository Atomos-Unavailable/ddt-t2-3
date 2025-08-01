from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
root = Tk()
root.destroy()
#creating a function that replaces the first gui with the second
#^ creating a comment so that I understand/remind myself of what is going on, and to tell others (including myself) what's happening so that things are easier to change; future proofing.
class upham:
        name = ""
        room = 0
u1=upham()
u1.name="Upham-1"
u1.room=1
u2=upham()
u2.name="Upham-2"
u2.room=2
u3=upham()
u3.name="Upham-3"
u3.room=3
u4=upham()
u4.name="Upham-4"
u4.room=4
u5=upham()
u5.name="Upham-5"
u5.room=5
u6=upham()
u6.name="Upham-6"
u6.room=6
u7=upham()
u7.name="Upham-7"
u7.room=7
u8=upham()
u8.name="Upham-8"
u8.room=8
u9=upham()
u9.name="Upham-9"
u9.room=9
u10=upham()
u10.name="Upham-10"
u10.room=10
class snell:
        name = ""
        room = 0
s1=snell()
s1.name="Snell-1"
s1.room=1
s2=snell()
s2.name="Snell-2"
s2.room=2
s3=snell()
s3.name="Snell-3"
s3.room=3
s4=snell()
s4.name="Snell-4"
s4.room=4
s5=snell()
s5.name="Snell-5"
s5.room=5
s6=snell()
s6.name="Snell-6"
s6.room=6
s7=snell()
s7.name="Snell-7"
s7.room=7
s8=snell()
s8.name="Snell-8"
s8.room=8
s9=snell()
s9.name="Snell-9"
s9.room=9
s10=snell()
s10.name="Snell-10"
s10.room=10
s11=snell()
s11.name="Snell-11"
s11.room=11

 
def Upham_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="lightblue")
        root.title("Upham / the best house")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_upham = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        combobox = ttk.Combobox(root, textvariable=selected_option_upham, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        #NEXT TASK: WRITE IN THE COMMAND TO COLLECT THESE VALUES AND READ THEM SO IT WILL TAKE USER TO THE CORRECT LOCATION
        root.mainloop()
def TK_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="blue")
        root.title("Tekanawa")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_tekanawa = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        combobox = ttk.Combobox(root, textvariable=selected_option_tekanawa, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        #NEXT TASK: read 'upham' command for more details
        root.mainloop()
def Kupe_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="yellow")
        root.title("Kupe")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_kupe = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
        combobox = ttk.Combobox(root, textvariable=selected_option_kupe, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        root.mainloop()
def Batten_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="grey")
        root.title("Batten")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_batten = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]
        combobox = ttk.Combobox(root, textvariable=selected_option_batten, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        root.mainloop()
def Snell_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="black")
        root.title("Snell")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_snell = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        combobox = ttk.Combobox(root, textvariable=selected_option_snell, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        root.mainloop()
def Rutherford_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="red")
        root.title("Rutherford")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_rutherford = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        combobox = ttk.Combobox(root, textvariable=selected_option_rutherford, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        root.mainloop()
def Hillary_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="green")
        root.title("Hillary")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_hillary = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        combobox = ttk.Combobox(root, textvariable=selected_option_hillary, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        root.mainloop()
def Mansfield_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.title("Mansfield")
        root.configure(bg="purple")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_mansfeild = StringVar()
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        combobox = ttk.Combobox(root, textvariable=selected_option_mansfeild, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        root.mainloop()
def Other_Blocks_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.configure(bg="white")
        root.title("other block")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        selected_option_other = StringVar()
        options = ["Language/L", "Techblock/TB", "Interntional/IB", "ESOL/E", "Design/D", "Four block/4.x", "Physics/P7", "Science block/SB", "Art/A", "Grym/G", "Computer/C"]
        combobox = ttk.Combobox(root, textvariable=selected_option_other, values=options)
        #set a default
        combobox.set(options[0])
        combobox.pack(side=TOP)
        root.mainloop()
def open_window2eng(root):
    #killing the first
    root.destroy()
    #creating the second
    root = Tk()
    root.title("hello")
    root.minsize(200,200)
    root.maxsize(1080, 1080)
    #Setting up the frames of this root to make sure it all works, and to set up the title of thsi page.
    eng_main_title = Frame(root, bg="grey")
    eng_main_title.pack(side=TOP, fill=X)
    eng_main_title_l = Label(eng_main_title, text="Welcome to the Mac-Change Map", wraplength=200, font="TkDefaultFont")
    eng_main_title_l.pack(side=TOP, fill=X)
    #creating a frame for the textbox and button to go on
    room_frame = Frame(root, bg="grey")
    room_frame.pack(side=TOP, fill=X)
    room_frame_label = Label(room_frame,text="lorem ipsuim", bg="grey")
    room_frame_label.pack(side=TOP, fill=X)
    room_code_label = ttk.Label(room_frame, text="Please enter the room code (the 2-3 character code of the 'room number') in the box below")
    room_code_label.pack(side=TOP, fill=X)
    room_code = StringVar()
    room_code_entry = ttk.Entry(room_frame, textvariable=room_code)
    room_code_entry.pack(side=TOP, fill=X)
    room_code_entry.focus()
    #creating button
    enter_button = Button(room_frame, bg="grey", relief=SUNKEN, borderwidth=5, text="Proceed to search", command =lambda: filler_command(root))
    enter_button.pack(side=BOTTOM, fill=X)
    #creating a description frame at the bottom to explain the pourpose of this appliacation
    eng_main_desc = Frame(root, bg="grey", relief=SUNKEN, borderwidth=5)
    eng_main_desc.pack(side=TOP, fill=X)
    eng_main_desc_l = Label(eng_main_desc, text="Our goal is to help people who aren't good with maps, people who do not speak english fluently, and just anyone in need of it. Here at Macleans we like to help people, so this is to help you find your way around the school if you are lost, or to find a location you have never been to before. Infact, we will also give you backstory about the general location, and point out wht sorts of activities take place in that area.", wraplength=375, font="TkDefaultFont")
    eng_main_desc_l.pack(side=TOP, fill=X)
    root.mainloop()
#creating a notisable filler command to see if buttons work
def filler_command(root):
        root.destroy()
        #creating the next frame
        root = Tk()
        root.title("house/block")
        root.minsize(200,200)
        root.maxsize(1080, 1080)
        enter_button1 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="Upham/U", command =lambda: Upham_command(root))
        enter_button1.pack(side=TOP, fill=X)
        enter_button2 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="Snell/S", command =lambda: Snell_command(root))
        enter_button2.pack(side=TOP, fill=X)
        enter_button3 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="TK/Tekanawa/T", command =lambda: TK_command(root))
        enter_button3.pack(side=TOP, fill=X)
        enter_button4 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="Batten/B", command =lambda: Batten_command(root))
        enter_button4.pack(side=TOP, fill=X)
        enter_button5 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="Hillary/H", command =lambda: Hillary_command(root))
        enter_button5.pack(side=TOP, fill=X)
        enter_button6 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="Kupe/K", command =lambda: Kupe_command(root))
        enter_button6.pack(side=TOP, fill=X)
        enter_button7 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="Rutherford/R", command =lambda: Rutherford_command(root))
        enter_button7.pack(side=TOP, fill=X)
        enter_button8 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="Mansfield/M", command =lambda: Mansfield_command(root))
        enter_button8.pack(side=TOP, fill=X)
        enter_button9 = Button(root, bg="grey", relief=SUNKEN, borderwidth=5, text="4./P/SB/TB/IB/E/G/A/D/C/L", command =lambda: Other_Blocks_command(root))
        enter_button9.pack(side=TOP, fill=X)
        root.mainloop()

    

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
proceed_b = Button(language_f, bg="white", relief=SUNKEN, text="Proceed : english", command=lambda:open_window2eng(root))
proceed_b.pack(side=BOTTOM, fill=X)
#ensuring the GUI stays running rather than dissapearing after it loads or remaining until the root is replaced with a different one
root.mainloop()
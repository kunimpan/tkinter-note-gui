from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import scrolledtext

#root window
root=Tk()
root.title("Note Application")
root.iconbitmap("icons/note.ico")
root.geometry("600x600")
root.resizable(0, 0)
root.config(bg="#6c8099")


def changeFont(e):
    if fontStyle.get() == "none":
        myFont=(fontFamily.get(), fontSize.get()) #font(name, style)
    else:
        myFont=(fontFamily.get(), fontSize.get(), fontStyle.get()) #font(name, size, style)

    textArea.config(font=myFont)

#settings
menu_color="#dbdadb"
text_color="white"

#design frame
menuFrame=Frame(root, bg=menu_color)
textFrame=Frame(root, bg=text_color)
menuFrame.pack(padx=5, pady=5)
textFrame.pack(padx=5, pady=5)

#menu button
new_img=ImageTk.PhotoImage(Image.open("icons/new.png"))
btnNew=Button(menuFrame, image=new_img)
btnNew.grid(row=0, column=0, padx=5, pady=5)

open_img=ImageTk.PhotoImage(Image.open("icons/open.png"))
btnOpen=Button(menuFrame, image=open_img)
btnOpen.grid(row=0, column=1, padx=5, pady=5)

save_img=ImageTk.PhotoImage(Image.open("icons/save.png"))
btnSave=Button(menuFrame, image=save_img)
btnSave.grid(row=0, column=2, padx=5, pady=5)

quit_img=ImageTk.PhotoImage(Image.open("icons/quit.png"))
btnQuit=Button(menuFrame, image=quit_img)
btnQuit.grid(row=0, column=3, padx=5, pady=4)

#font options
allFonts = font.families() #All fonts in your device.
fontFamily=StringVar() #Keep font.
fontOption=OptionMenu(menuFrame, fontFamily, *allFonts, command=changeFont)
fontFamily.set("Arial")
fontOption.config(width=20)
fontOption.grid(row=0, column=4, padx=5, pady=5)

#size option
sizes=[8, 12, 18, 25, 36, 42, 50]
fontSize=IntVar()  #Keep font size.
sizeOption = OptionMenu(menuFrame, fontSize, *sizes, command=changeFont)
fontSize.set(12)
sizeOption.config(width=5)
sizeOption.grid(row=0, column=5, padx=5, pady=5)

#style option
styles=["none", "bold", "italic"]
fontStyle = StringVar()
styleOption = OptionMenu(menuFrame, fontStyle, *styles, command=changeFont)
fontStyle.set("none")
styleOption.config(width=10)
styleOption.grid(row=0, column=6, padx=5, pady=5)

#scroll text
myFont=(fontFamily.get(), fontSize.get())
textArea = scrolledtext.ScrolledText(textFrame, bg=text_color, font=myFont, width=1000, height=1000)
textArea.pack()

root.mainloop()
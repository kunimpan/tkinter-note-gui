from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

#root window
root=Tk()
root.title("Note Application")
root.iconbitmap("icons/note.ico")
root.geometry("600x600")
root.resizable(0, 0)
root.config(bg="#6c8099")

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
fontOption=OptionMenu(menuFrame, fontFamily, *allFonts)
fontFamily.set("Arial")
fontOption.config(width=20)
fontOption.grid(row=0, column=4, padx=5, pady=5)

root.mainloop()
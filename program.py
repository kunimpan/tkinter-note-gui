from tkinter import *

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

root.mainloop()
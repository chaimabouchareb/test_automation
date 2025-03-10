from tkinter import *
master_window = Tk()
master_window.geometry("500x300")
master_window.title("StringVar Example")
tape_word=StringVar()
word_box=Entry(master_window, textvariable=tape_word)
word_box.grid=(columnspan:=4, ipadx:=70)
master_window.mainloop()


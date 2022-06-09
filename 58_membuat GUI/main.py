import tkinter as tk

root = tk.Tk()
def event_tombol():
    label2 = tk.Label(root,text="by nurdiansyahRM")
    label2.pack()


label = tk.Label(root,text="hallo dunia \n ini adalah gui sederhana\n menggunakan python")
tombol = tk.Button(root,text="Klik",command =event_tombol())

label.pack()
tombol.pack()

root.mainloop()
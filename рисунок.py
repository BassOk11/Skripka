import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
canvas.create_rectangle(200, 170, 150, 100)
window.mainloop()

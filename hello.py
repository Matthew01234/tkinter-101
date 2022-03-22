import tkinter
window = tkinter.Tk()

window.geometry('200x200')
window.configure(background='black')
box1 = tkinter.Label(
    window,
    text="Hello\n Tkinter!",
    bg="red",
    fg="white"
)
box1.pack(
    ipadx=50,
    ipady=50
)
box1.pack(
    ipadx=10,
    ipady=10,
    expand=True
)
window.mainloop()
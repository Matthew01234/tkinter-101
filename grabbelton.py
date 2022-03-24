import tkinter
import random
window = tkinter.Tk()
box1 = tkinter.Label(window)

window.title('Grabbelton')
window.geometry('400x400')
regenboogbg = ['red','orange','yellow','green','purple','blue']
item = ['nee', 'Tv','kaas','zaadjes','shitty iphone batterij','tafeblad','wieldop','melk zonder pak','albert heijn', 'pak zonder melk', 'geen melk en geen pak', 'pan bami zonder satesaus', 'zacht gekookt eitje', 'clown', 'corona', 'freddy fazzbear', 'clahs of clans battlepass', 'no bitches', 'panzerkanpfwagen', 'boeing 777', 'Big Linde heftruck - BG56580 \n Van kunststof \n Heftruck Pallet \n 1030x570x1070 mm', 'iets roods', 'brazil', 'Boeing AH-64 \nApache attack chopper', 'mike zn crappy pc']
random.shuffle(item)

i = 0
def grabelitem():
    
    box1.configure(
        text=f"Gefeliciteerd,\nje hebt {item.pop(0)}\n gegrabbeld!",
        bg="red",
        fg="white",
        font=(40)
    )
    box1.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    if len(item) == 0:
        box1.configure(
        text=('EMPTY'))
        
    box1.place(rely=0.7,relx=0.5,anchor=tkinter.CENTER)
button = tkinter.Button(window,width=50, height=50,command=grabelitem)
button.pack()
button.configure(text='GRABBELLEN')
button.place(relwidth=0.8, relheight=0.3, rely=0.3, relx=0.5, anchor=tkinter.CENTER)


while True:
    window.configure(bg= regenboogbg[i % 6])
    window.update()
    i += 1

window.mainloop()
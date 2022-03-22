import tkinter
from time import sleep

window = tkinter.Tk()

window.title('explosiefvenster')
window.configure(background='yellow')
COLOR = ['white','yellow','orange','red','purple','black','black']
def aftellen():
    for i in range(1,8):
        sleep(2)
        print(7-i)
        window.configure(background=COLOR[i-1])
        window.geometry(f'{50 * i}x{50 * i}')
        window.update() 
    print ('BOOM!') 
    window.destroy()
    
    
aftellen()
window.mainloop()
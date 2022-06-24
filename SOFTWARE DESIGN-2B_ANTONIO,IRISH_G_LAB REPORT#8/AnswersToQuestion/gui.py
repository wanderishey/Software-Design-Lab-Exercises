import tkinter as tk
root = tk.Tk() 
root.configure(background='bisque')
def pressed():
    print("Button pressed")

def create_layout(frame): 
    b1= tk.Button (frame, text='Button1', bg="grey", command=pressed)
    b1.pack(side='top', anchor = 'w', pady = '20px')
    b2 = tk.Button(frame, text='Button2', bg='grey', command=pressed, padx='20')
    b2.pack(side='left')

frame = tk.Frame(root, background = 'bisque')
create_layout(frame)
frame.place(anchor = 'nw')
root.geometry('300x300')
root.mainloop()
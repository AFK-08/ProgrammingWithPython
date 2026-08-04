import tkinter

## Screen
window = tkinter.Tk()
window.title("My GUI Program!")
window.minsize(width=500,height=500)
window.config(padx=100,pady=100)


## Labels

my_label = tkinter.Label(text="I am a Label",font=("Arial",15,"bold"))
my_label.grid(column=0,row=0)
my_label.config(text="New Text")


## Buttons:

def buttonClicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click me.",background="white",command=buttonClicked)

button.grid(column=0,row=1)


## Entry:

input = tkinter.Entry(width=13)
input.grid(column=0,row=2)


## for other widgets use Documentation---







window.mainloop()
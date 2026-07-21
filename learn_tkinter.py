import tkinter

## Screen
window = tkinter.Tk()
window.title("My GUI Program!")
window.minsize(width=500,height=500)

## Labels

my_label = tkinter.Label(text="I am a Label",font=("Arial",15,"bold"))
my_label.pack(side="left")

my_label = tkinter.Label(text="This is another Label ")
my_label.pack(side="top")










window.mainloop()
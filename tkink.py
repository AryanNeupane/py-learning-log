from tkinter import *

def submit():
    texts=entry.get()
    print("Submitted")
    print("text :", texts)

win=Tk()

win.title("meroApp")
win.iconbitmap("icon.ico")

# win.config(bg="red")
win['bg']="orange"

win.geometry("300x500")
label=Label(win,text="Hello World",
            font=("Arial",16,'bold'),
            fg="#00ff00",
            bg="gray",
            padx=20,
            pady=10)
label.pack()
# label.place(x=10,y=10)

button=Button(win,text="click me",
              )
button.pack()
                          


checkbtn=Checkbutton(win,text="I agree")
checkbtn.pack()



win.mainloop()
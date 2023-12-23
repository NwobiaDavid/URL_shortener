from tkinter import *
import pyshorteners

window = Tk()
window.title('URL Shortener')
icon = PhotoImage(file='C:\\Users\\Nwobia David\\Downloads\\XAES.png')
window.iconphoto(True, icon)
window.geometry('500x800')

def shorten():
    if entry2.get():
        entry2.delete(0, END)

    if entry.get():
        url = pyshorteners.Shortener().tinyurl.short(entry.get())
        entry2.insert(END, url)

        print(pyshorteners.Shortener().tinyurl.expand(url))

label = Label(window, text='enter the link to shorten', font=('poppins', 28))
label.pack(pady=20)

entry = Entry(window, font=('poppins', 22))
entry.pack(pady=20)

btn = Button(window, text='shorten link', command=shorten, font=('poppins', 24))
btn.pack(pady=20)

label2 = Label(window, text='shortened link', font=('Poppins', 20))
label2.pack(pady=50)

entry2 = Entry(window, font=('poppins', 22), justify=CENTER, width=30, bd=0, bg='systembuttonface' )
entry2.pack(pady=10)


window.mainloop()

from tkinter import *
import pyshorteners
from tkinter import messagebox

def shorten():
    if entry2.get():
        entry2.delete(0, END)

    if entry.get():
        try:
            url = pyshorteners.Shortener().tinyurl.short(entry.get())
            entry2.insert(END, url)
            print(pyshorteners.Shortener().tinyurl.expand(url))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def copy_to_clipboard():
    if entry2.get():
        window.clipboard_clear()
        window.clipboard_append(entry2.get())
        window.update()
        messagebox.showinfo("Success", "Shortened link copied to clipboard!")

# Set up the main window
window = Tk()
window.title('URL Shortener')
icon = PhotoImage(file='C:\\Users\\Nwobia David\\Downloads\\XAES.png')
window.iconphoto(True, icon)
window.geometry('500x400')

# Create and pack widgets
label = Label(window, text='Enter the link to shorten', font=('poppins', 18))
label.pack(pady=10)

entry = Entry(window, font=('poppins', 14))
entry.pack(pady=10)

btn_shorten = Button(window, text='Shorten Link', command=shorten, font=('poppins', 16))
btn_shorten.pack(pady=10)

label2 = Label(window, text='Shortened Link', font=('Poppins', 16))
label2.pack(pady=20)

entry2 = Entry(window, font=('poppins', 14), justify=CENTER, width=30, bd=0, bg='systembuttonface')
entry2.pack(pady=10)

btn_copy = Button(window, text='Copy to Clipboard', command=copy_to_clipboard, font=('poppins', 14))
btn_copy.pack(pady=10)

window.mainloop()

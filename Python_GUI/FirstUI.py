import tkinter as tk
def showtext():
    print(entry.get())

window = tk.Tk()

label = tk.Label(text="Welcom to Python GUI")
label.pack()

label_1 = tk.Label(text="Enter any text: ")
label_1.pack()
entry = tk.Entry()
entry.pack()

btn = tk.Button(text="Close", width=6, height=3, command=showtext)
btn.pack()

window.mainloop()

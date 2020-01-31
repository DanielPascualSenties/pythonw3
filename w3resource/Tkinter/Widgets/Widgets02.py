import tkinter as tk

app = tk.Tk()
app.geometry('200x100')
app.resizable(0,0)
app.title('Banana')
can = tk.Canvas(app, width=200, height= 100)
can.pack()
can.create_rectangle(10, 20, 190, 80, fill="#ff0000")

app.mainloop()

import tkinter as tk

app = tk.Tk()
app.geometry('400x100')
app.title('Banana')
label = tk.Label(app, text="Galleta", font=("Arial Bold", 40))
label.grid(row=0, column=0)

app.mainloop()

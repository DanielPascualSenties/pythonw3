import tkinter as tk

app = tk.Tk()
app.geometry('600x300')
app.resizable(0,0)
app.title('Banana')
label = tk.Label(app, text="Galleta", font=("Arial Bold", 20))
label.grid(row=0, column=0)
bu = tk.Button(app, text="Despegue")
bu.grid(row=1, column=0)


app.mainloop()

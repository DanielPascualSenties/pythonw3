import tkinter as tk


def say_hello():
    print("Hello")


app = tk.Tk()
app.geometry('600x300')
app.resizable(0,0)
app.title('Banana')
label = tk.Label(app, text="Galleta", font=("Arial Bold", 20))
label.grid(row=0, column=0)
bu = tk.Button(app, text="Hello", command=say_hello)
bu.grid(row=1, column=0)
bu = tk.Button(app, text="Exit", command= quit)
bu.grid(row=1, column=1)

app.mainloop()

import tkinter as tk
from tkinter import ttk


app = tk.Tk()
app.geometry('400x100')
app.title('Crit finder 3.0')


def showchoice():
    print("<<ComboBoxSelected>>")


def callbackfunc(event):
    print("New Element Selected")


def resultstring():
    print("select, number = " + "3")


def showresult():
    type_crit = comboType.get()
    sever_crit = comboSeverity.get()
    roll_crit = entryRoll.get()
    print("select result from crits where type='" + str(type_crit) + "' and severity='" +
          str(sever_crit) + "' and roll ='" + str(roll_crit) + "'")


labelType = tk.Label(app,
                     text="Type of critical")
labelType.grid(column=0, row=0)

labelSeverity = tk.Label(app,
                         text="Severity")
labelSeverity.grid(column=1, row=0)

labelSeverity = tk.Label(app,
                         text="Roll")
labelSeverity.grid(column=2, row=0)

comboType = ttk.Combobox(app,
                         values=[
                             "Crush",
                             "Puncture",
                             "Slash",
                             "Heat",
                             "Cold",
                             "Lightning",
                             "Impact",
                             "Bite"])

comboType.grid(column=0, row=1)
comboType.current(0)

comboSeverity = ttk.Combobox(app,
                             values=[
                                 "A",
                                 "B",
                                 "C",
                                 "D",
                                 "E"])

comboSeverity.grid(column=1, row=1)
comboSeverity.current(0)

entryRoll = ttk.Entry(app, width=5, textvariable="resultString")
entryRoll.grid(column=3, row=1)

resultButton = tk.Button(app, text='Get Result',
                         command=showresult)
resultButton.grid(column=1, row=3)

comboType.bind("<<ComboBoxSelected>>", showresult)

app.mainloop()

import treatment.treatment_core
from tkinter import Tk, Label, Listbox
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


treatment_list = treatment.treatment_core.get_treatment_list()


def start():
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" +
                    str(window.winfo_screenheight()) + "+0+0")
    window.title('Treatment SAK')
    toptext = Label(window, text="Treatments List", width=window.winfo_screenwidth(),
                    height=window.winfo_screenheight() / 7)
    treatment_list_box = Listbox(window, selectmode='extended',
                                 height=6 / 7 * window.winfo_screenheight(), yscrollcommand=True)
    for i in range(len(treatment_list)):
        treatment_list_box.insert(i, treatment_list[i]["name"])

    treatment_list_box.bind("<<ListboxSelect>>", clicked)
    toptext.pack()
    treatment_list_box.pack()
    window.mainloop()


def clicked(event):
    w = event.widget
    index = int(w.curselection()[0])
    treatment_info = treatment_list[index]

    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" +
                    str(window.winfo_screenheight()) + "0+0")
    window.title('Treatment SAK - About ' + treatment_info["name"])

    toptext = Label(window, text=treatment_info["name"], width=window.winfo_screenwidth(),
                    height=window.winfo_screenheight() / 7)
    doctext = Label(window, text=treatment_info["document"], justify="left", width=window.winfo_screenwid(),
                    height=window.winfo_screenheight() * 6 / 7)

    toptext.pack()
    doctext.pack()

    window.mainloop()

from tkinter import *
import treatment.treatment_core

treatment_list = treatment.treatment_core.get_treatment_list()


def start():
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" + str(window.winfo_screenheight()))
    window.title('Treatment SAK')
    toptext = Label(window, text="Treatments List", width=window.winfo_screenwidth(),
                    height=window.winfo_screenheight() / 7)
    treatment_list_box = Listbox(window, selectmode='extended',
                                 height=6 / 7 * window.winfo_screenheight(), yscrollcommand=True)
    for i in range(len(treatment_list)):
        treatment_list_box.insert(i, treatment_list[i]["name"])

    treatment_list_box.bind("<<ListboxSelect>>", callback)
    toptext.pack()
    treatment_list_box.pack()
    window.mainloop()


def callback(event):
    w = event.widget
    index = int(w.curselection()[0])
    clicked(treatment_list[index])


def clicked(treatment):
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" + str(window.winfo_screenheight()))
    window.title('Treatment SAK - About ' + treatment["name"])
    toptext = Label(window, text=treatment["name"], width=window.winfo_screenwidth(),
                    height=window.winfo_screenheight() / 7)
    doctext = Label(window, text=treatment["document"], justify="left", width=window.winfo_screenwidth(),
                    height=window.winfo_screenheight() * 6 / 7)
    toptext.pack()
    doctext.pack()
    window.pack()

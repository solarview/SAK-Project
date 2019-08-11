from tkinter import Tk, Label, Listbox
import urllib.request
import json
import os
import sak_core


treatment_list = get_treatment_list()


def start_gui():
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


# id_treatment(id, name, version, document, images( id : image data //Not now))
# how to call image id in doc: $$0$$

def update_treatments():
    data = json.loads(
        urllib.request.urlopen(
            "http://sakproject.ml/treatments_list.json").read().decode())  # data ( id : integer , version : integer)
    if not os.path.isdir(sak_core.RESOURCE_DIR_PATH + "treatments"):
        os.mkdir(sak_core.RESOURCE_DIR_PATH + "treatments")
    for i in range(len(data)):
        if not os.path.isfile(sak_core.RESOURCE_DIR_PATH + "treatments/" + data[i]["id"] + "_treatment.sak"):
            f = open(i + "_treatment.sak", "w+")
            f.write(urllib.request.urlopen("http://sakproject.ml/" +
                                           i + "_treatments.sak").read().decode())
            f.close()
        else:
            f = open(i + "_treatment.sak", "r+")
            d = json.loads(f.read())
            if int(d["version"]) < data[i]["version"]:
                f.close()
                f = open(i + "_treatment.sak", "w+")
                f.write(urllib.request.urlopen(
                    "http://sakproject.ml/" + i + "_treatments.sak").read().decode())
                f.close()


def get_treatment_list() -> list:
    file_list = os.listdir(sak_core.RESOURCE_DIR_PATH + "treatments/")
    treatment_list = []
    for fname in file_list:
        f = open(sak_core.RESOURCE_DIR_PATH + "treatments/" + fname, "r+")
        treatment_list.append(json.loads(f.read())["name"])
    return treatment_list

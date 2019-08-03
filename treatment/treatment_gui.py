from tkinter import *
import treatment.treatment_core


class treatment_gui:

    def __init__(self):
        self.window = Tk()
        self.window.title('Treatment List')
        self.canvas = Canvas(self.window, width=700, height=800, bg="#FFFFFF")
        self.canvas.create_rectangle(0, 0, 700, 100, fill="red")
        self.canvas.create_text(350, 50, anchor="center",
                                font="Purisa",
                                text="Treatment list")
        self.count = 0
        for t in treatment.treatment_core.get_treatment_list():
            self.create_list_here(t)

    def start(self):
        self.canvas.pack()
        self.canvas.focus_set()
        self.canvas.mainloop()

    def create_list_here(self, treatment):
        def goback(event):
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 700, 100, fill="red")
            self.canvas.create_text(350, 50, anchor="center",
                                    font="Purisa",
                                    text="Treatment list")
            self.count = 0
            for t in treatment.treatment_core.get_treatment_list():
                self.create_list_here(t)

        def clicked(event):
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 700, 100, fill="red")
            self.canvas.create_text(350, 50, anchor="center",
                                    font="Purisa",
                                    text="Treatment about " + treatment["name"])
            self.canvas.create_rectangle(20, 20, 80, 80, fill="green", text="<-", tags="goback")
            self.canvas.tag_bind("goback", "<Button-1>", goback)
            documents = treatment["document"].split("$$")
            i = False
            y = 110
            for text in documents:
                i = not i
                if i:
                    tt = self.canvas.create_text(10, y, font="Purisa", text=text)
                else:
                    tt = self.canvas.create_image(10, y, PhotoImage())  # TODO use treatment["image"][text]
                y = self.canvas.bbox(tt)[3]

        self.count += 1
        self.canvas.create_rectangle(60 + 260 * (self.count % 3 - 1), 110 + 260 * (self.count / 3 - 1),
                                     260 * (self.count % 3), 310 + 260 * (self.count / 3 - 1), fill="green",
                                     tags=treatment["name"] + "_treatment_play")
        self.canvas.create_image(60 + 260 * (self.count % 3 - 1), 110 + 260 * (self.count / 3 - 1), PhotoImage(),
                                 tags=treatment["name"] + "_treatment_play")  # TODO use treatment["image"][0]
        self.canvas.create_rectangle(60 + 260 * (self.count % 3 - 1), 260 + 260 * (self.count / 3 - 1),
                                     260 * (self.count % 3), 310 + 260 * (self.count / 3 - 1), fill="blue",
                                     tags=treatment["name"] + "_treatment_play")
        self.canvas.create_text(160 + 260 * (self.count % 3 - 1), 285 + 260 * (self.count / 3 - 1), anchor="center",
                                font="Purisa",
                                text=treatment["name"], tags=treatment["name"] + "_treatment_play")
        self.canvas.tag_bind(treatment["name"] + "_treatment_play", "<Button-1>", clicked)

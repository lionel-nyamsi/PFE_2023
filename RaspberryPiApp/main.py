import customtkinter
import tkinter as tk
from PIL import Image, ImageTk

"""def recuperer(textbox):
    text = textbox.get(1.0, 'end')
    word = text.split()
    lastIndex = -1
    for i in word:
        lastIndex += 1
    return word[len(word)-1]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("liionpfe")
        self.minsize(600, 400)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 0), sticky="nsew")

        self.combobox = customtkinter.CTkComboBox(master=self, values=[""])
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Insert Text")
        self.button.grid(row=1, column=1, padx=0, pady=20, sticky="ew")
        self.button1 = customtkinter.CTkButton(master=self, command=self.boutton_recupere, text="Get Text")
        self.button1.grid(row=1, column=2, padx=20, pady=20, sticky="ew")
        self.button2 = customtkinter.CTkButton(master=self, command=self.boutton_efface, text="Wipe")
        self.button2.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        self.textbox.insert("insert", self.combobox.get() + "\n")

    def boutton_efface(self):
        self.textbox.delete(1.0,"end")

    global value
    value = [""]

    def boutton_recupere(self):
        global value
        value += [recuperer(self.textbox)]
        self.combobox.configure(values=value)
        self.textbox.insert("insert", "\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()"""


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("597x417")
        self.title("Liion")
        self.minsize(597, 417)

        # create 2x2 grid system
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # = customtkinter.CTkImage(light_image=Image.open("venv/images/logo.png"), size=(50, 50))
        logo = ImageTk.PhotoImage(master=self, light_image=Image.open("venv/images/logo.png"))
        self.frame.grid(row=1, column=1, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()

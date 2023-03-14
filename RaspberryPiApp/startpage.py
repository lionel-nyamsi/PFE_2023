import customtkinter
import PIL.Image


class StartPage(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        customtkinter.CTkFrame.__init__(self, parent)

        # app configuration
        self.configure(fg_color=app.default_bg_color, corner_radius=0)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #
        frame = customtkinter.CTkFrame(self, fg_color=app.default_bg_color)
        frame.grid(row=1, column=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=0)
        frame.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"),
                                      size=(int(128 * app.scale), int(164 * app.scale)))
        photo = customtkinter.CTkLabel(frame, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e")
        label1 = customtkinter.CTkLabel(frame, text="LIION ASSIST", height=int(14 * app.scale),
                                        font=customtkinter.CTkFont(family="Inter", size=int(20 * app.scale)),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame, text="STAY FOCUSED ON THE ROAD", height=int(10 * app.scale),
                                        font=customtkinter.CTkFont(family="Inter", size=int(10 * app.scale)),
                                        text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

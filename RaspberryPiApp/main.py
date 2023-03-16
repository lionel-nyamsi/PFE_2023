import customtkinter
import startpage
import connectionpage
import home_page
import page_icone1
import page_icone2
import page_icone3
import page_icone4
import page_icone5
import page_icone6


class App(customtkinter.CTk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        self.scale = 1
        self.default_text_color = "#C9C5C5"
        self.default_bg_color = "#0F0332"
        self.default_bar_color = "#39585B"
        self.default_text_size = 12 * self.scale
        self.home_icon_dimen = 50 * self.scale
        self.default_icon_dimen = 70 * self.scale

        self.geometry("836x584")
        self.title("LIION ASSIST")
        self.minsize(int(836), int(584))
        self.maxsize(int(836), int(584))
        self.configure(fg_color="#001200")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # creating a container
        if self.scale >= 1:
            nsew = 'nsew'
        else:
            nsew = ''
        container = customtkinter.CTkFrame(self,
                                           corner_radius=0)  # , width=int(1836*App.scale), height=int(584*App.scale))
        container.grid(row=0, column=0, sticky=nsew)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
                startpage.StartPage, connectionpage.ConnectionPage, home_page.HomePage, page_icone1.PageIcon1, page_icone2.PageIcon2, page_icone3.PageIcon3, page_icone4.PageIcon4, page_icone5.PageIcon5, page_icone6.PageIcon6):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(StartPage)
        self.after(0, self.show_frame, startpage.StartPage)
        self.after(2500, self.show_frame, connectionpage.ConnectionPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()

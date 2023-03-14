import customtkinter
import PIL.Image
import home_page


class PageIcon4(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=app.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(app.home_icon_dimen),
                                            fg_color=app.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(app.home_icon_dimen),
                                                                                               int(app.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(app.home_icon_dimen),
                                             height=int(app.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=app.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=app.default_bar_color,
                                            width=int(app.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=app.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(app.default_text_size + 8 * app.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=app.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(app.default_text_size - 2 * app.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        #
        frame_video = customtkinter.CTkFrame(barinf_cadre, width=int(app.home_icon_dimen),
                                             fg_color=app.default_bar_color)
        frame_video.grid(row=1, column=0, pady=20, sticky='esw')
        frame_video.grid_rowconfigure(0, weight=1)
        img_video = customtkinter.CTkImage(light_image=PIL.Image.open("images/video.png"),
                                           size=(int(app.home_icon_dimen), int(app.home_icon_dimen)))
        image_video = customtkinter.CTkButton(frame_video, width=int(app.home_icon_dimen),
                                              height=int(app.home_icon_dimen), image=img_video, text="",
                                              command=lambda: app.show_frame(home_page.HomePage), fg_color=app.default_bar_color)
        image_video.grid(row=0, column=0)

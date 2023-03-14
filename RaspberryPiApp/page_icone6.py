import customtkinter
import PIL.Image
import home_page


class PageIcon6(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=app.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1, uniform='same_group')
        self.grid_columnconfigure(2, weight=1, uniform='same_group')

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
        frame_sms = customtkinter.CTkFrame(barinf_cadre, width=int(app.home_icon_dimen),
                                           fg_color=app.default_bar_color)
        frame_sms.grid(row=1, column=0, pady=20, sticky='esw')
        frame_sms.grid_rowconfigure(0, weight=1)
        img_sms = customtkinter.CTkImage(light_image=PIL.Image.open("images/sms.png"),
                                         size=(int(app.home_icon_dimen), int(app.home_icon_dimen)))
        image_sms = customtkinter.CTkButton(frame_sms, width=int(app.home_icon_dimen),
                                            height=int(app.home_icon_dimen), image=img_sms, text="",
                                            command=lambda: app.show_frame(home_page.HomePage), fg_color=app.default_bar_color)
        image_sms.grid(row=0, column=0)

        #
        title_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#D9D9D9", height=30)
        title_frame.grid(row=0, column=1, rowspan=1, columnspan=2, sticky="nesw")

        #
        right_frame = customtkinter.CTkScrollbar(self, corner_radius=0, fg_color="#FFFFFF")
        right_frame.grid(row=1, column=1, rowspan=3, columnspan=1, sticky="nesw")
        right_frame.grid_columnconfigure(0, weight=1)

        search_bar = customtkinter.CTkEntry(right_frame, height=30, corner_radius=15, fg_color="#D9D9D9",
                                            text_color="#4E4C4C", placeholder_text="Rechercher des conversations",
                                            border_color="#D9D9D9")
        search_bar.grid(row=0, column=0, padx=10, pady=15, sticky='ew')
        dicussion1 = Discussion(right_frame, "papa", 9)
        dicussion1.creer_right(1)
        dicussion2 = Discussion(right_frame, "armel", 9)
        dicussion2.creer_right(2)
        dicussion3 = Discussion(right_frame, "M. farouche", 9)
        dicussion3.creer_right(3)
        dicussion4 = Discussion(right_frame, "M. farouche", 9)
        dicussion4.creer_right(4)
        dicussion5 = Discussion(right_frame, "M. farouche", 9)
        dicussion5.creer_right(5)
        dicussion6 = Discussion(right_frame, "M. farouche", 9)
        dicussion6.creer_right(6)
        dicussion7 = Discussion(right_frame, "M. farouche", 9)
        dicussion7.creer_right(7)
        dicussion8 = Discussion(right_frame, "M. farouche", 9)
        dicussion8.creer_right(8)

        #
        global left_frame
        left_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#BCDAFF")
        left_frame.grid(row=1, column=2, rowspan=3, columnspan=1, sticky="nesw")
        dicussion1.creer_left(left_frame)


class Discussion:
    color = "#1E7910"

    def __init__(self, parent, nom, numero):
        self.nom = nom
        self.numero = numero
        self.parent = parent
        self.height = 50

    def creer_right(self, ligne):
        theme_color = "#D9D9D9"
        label_color = "#000000"
        msg_color = "#4E4C4C"
        container = customtkinter.CTkButton(self.parent, height=self.height, fg_color=theme_color, corner_radius=12,
                                            text="", hover_color=theme_color)
        container.grid(row=ligne, column=0, padx=10, pady=5, sticky="ew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=0)
        container.grid_columnconfigure(0, weight=0)
        container.grid_columnconfigure(1, weight=1)

        cercle = customtkinter.CTkFrame(container, fg_color=Discussion.color, height=50, width=50, corner_radius=25)
        cercle.grid(row=0, column=0, rowspan=2, padx=5)
        frame_cercle = customtkinter.CTkLabel(container, fg_color=Discussion.color, height=18, width=18,
                                              text=self.nom[0].upper(),
                                              font=customtkinter.CTkFont(family="Inter", size=30, weight="bold"))
        frame_cercle.grid(row=0, column=0, rowspan=2, padx=5)

        frame_nom = customtkinter.CTkButton(container, height=int(self.height * 3 / 5), fg_color=theme_color,
                                            text="", hover_color=theme_color,
                                            command=lambda: self.creer_left(left_frame))
        frame_nom.grid(row=0, column=1, padx=10, sticky="nsew")
        frame_nom.grid_rowconfigure(0, weight=1)
        frame_nom.grid_columnconfigure(0, weight=1)
        frame_nom.grid_columnconfigure(1, weight=1)
        label_nom = customtkinter.CTkButton(frame_nom, text_color=label_color, fg_color=theme_color,
                                            hover_color=theme_color, text=self.nom.title(), anchor='w',
                                            font=customtkinter.CTkFont(family="Inter", size=20, weight="bold"),
                                            command=lambda: self.creer_left(left_frame))
        label_nom.grid(row=0, column=0, sticky="w")
        label_time = customtkinter.CTkButton(frame_nom, text_color=label_color, fg_color=theme_color, anchor='e',
                                             hover_color=theme_color, text="07:38",
                                             font=customtkinter.CTkFont(family="Inter", size=15, weight="bold"),
                                             command=lambda: self.creer_left(left_frame))
        label_time.grid(row=0, column=1, sticky='e')

        frame_msg = customtkinter.CTkButton(container, height=int(self.height * 2 / 5), fg_color=theme_color,
                                            text="", hover_color=theme_color,
                                            command=lambda: self.creer_left(left_frame))
        frame_msg.grid(row=1, column=1, sticky="w")
        frame_msg.grid_rowconfigure(0, weight=1)
        frame_msg.grid_columnconfigure(0, weight=1)
        label_msg = customtkinter.CTkButton(frame_msg, text="je vais bien", text_color=msg_color, fg_color=theme_color,
                                            font=customtkinter.CTkFont(family="Inter", size=12),
                                            hover_color=theme_color, anchor='w',
                                            command=lambda: self.creer_left(left_frame))
        label_msg.grid(row=0, column=0, padx=9, sticky="w")

    def creer_left(self, parent):
        theme_color = "#D9D9D9"
        label_color = "#000000"
        entete_color = "#6C0590"
        parent.grid_rowconfigure(0, weight=0)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        entete = customtkinter.CTkFrame(parent, height=30, fg_color=entete_color, corner_radius=0)
        entete.grid(row=0, column=0, columnspan=2, sticky="ew")
        entete_label = customtkinter.CTkLabel(entete, text=self.nom.title())
        entete_label.grid()

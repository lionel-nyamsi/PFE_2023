import customtkinter
import PIL.Image
import page_icone1
import page_icone2
import page_icone3
import page_icone4
import page_icone5
import page_icone6


class Icon:
    nombre_cree = 0

    def __init__(self, parent, nom, police, source_image, taille, xligne, ycolone):
        Icon.nombre_cree += 1
        self.parent = parent
        self.nom = nom
        self.police = int(police)
        self.source_image = source_image
        self.taille = int(taille)
        self.xligne = xligne
        self.ycolone = ycolone

    def creer(self, app):
        frame = customtkinter.CTkFrame(self.parent, width=self.taille, height=self.taille, fg_color="#0F0332")
        frame.grid(row=self.xligne, column=self.ycolone, padx=5)
        frame.grid_rowconfigure(0)
        frame.grid_rowconfigure(1)
        global a
        a = app
        program = """img = customtkinter.CTkImage(light_image=PIL.Image.open(self.source_image), size=(self.taille, 
        self.taille))\nimage = customtkinter.CTkButton(frame, width=self.taille, fg_color="#0F0332", 
        height=self.taille, image=img, text="", command= lambda: a.show_frame(page_icone""" + str(
            Icon.nombre_cree) + """.PageIcon""" + str(Icon.nombre_cree) + \
                  ")) \nimage.grid(row=0, column=0)"
        exec(program)
        label = customtkinter.CTkLabel(frame, text=self.nom, fg_color="#0F0332",
                                       font=customtkinter.CTkFont(family="Inter", size=self.police),
                                       text_color="#FFFFFF")
        label.grid(row=1, column=0)


class HomePage(customtkinter.CTkFrame):
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
        frame_logo = customtkinter.CTkFrame(self, fg_color=app.default_bg_color, width=100)
        frame_logo.grid(row=1, column=2)
        frame_logo.grid_rowconfigure(0, weight=1)
        frame_logo.grid_rowconfigure(1, weight=0)
        frame_logo.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(92, 117))
        photo = customtkinter.CTkLabel(frame_logo, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e")
        label1 = customtkinter.CTkLabel(frame_logo, text="LIION ASSIST", height=14,
                                        font=customtkinter.CTkFont(family="Inter", size=15),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame_logo, text="STAY FOCUSED ON THE ROAD", height=10,
                                        font=customtkinter.CTkFont(family="Inter", size=7), text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

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

        # cadre des icones
        barnav_frame = customtkinter.CTkFrame(self, fg_color=app.default_bg_color)
        barnav_frame.grid(row=2, column=1, rowspan=1, columnspan=3)

        #
        Icon.nombre_cree = 0
        phone_icon = Icon(barnav_frame, "Telephone", app.default_text_size, "images/phone.png",
                          app.default_icon_dimen, 0, 0)
        phone_icon.creer(app)
        gps_icon = Icon(barnav_frame, "GPS", app.default_text_size, "images/gps.png",
                        app.default_icon_dimen, 0, 1)
        gps_icon.creer(app)
        musique_icon = Icon(barnav_frame, "Music", app.default_text_size, "images/music.png",
                            app.default_icon_dimen, 0, 2)
        musique_icon.creer(app)
        video_icon = Icon(barnav_frame, "Videos", app.default_text_size, "images/video.png",
                          app.default_icon_dimen, 0, 3)
        video_icon.creer(app)
        settings_icon = Icon(barnav_frame, "Parametres", app.default_text_size, "images/settings.png",
                             app.default_icon_dimen, 0, 4)
        settings_icon.creer(app)
        sms_icon = Icon(barnav_frame, "Messages", app.default_text_size, "images/sms.png",
                        app.default_icon_dimen, 0, 5)
        sms_icon.creer(app)

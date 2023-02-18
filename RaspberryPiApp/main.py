import customtkinter
import PIL.Image
import qrcode


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # activities(pages) configuration
        self.default_text_color = "#C9C5C5"
        self.default_bg_color = "#0F0332"
        self.default_bar_color = "#39585B"
        self.default_text_size = 12
        self.home_icon_dimen = 50
        self.default_icon_dimen = 70

        # app configuration
        self.geometry("835.8x583.8")
        self.title("LIION ASSIST")
        self.minsize(836, 584)
        self.maxsize(836, 584)
        self.configure(fg_color=self.default_bg_color)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #
        frame = customtkinter.CTkFrame(self, fg_color=self.default_bg_color)
        frame.grid(row=1, column=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=0)
        frame.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(128, 164))
        photo = customtkinter.CTkLabel(frame, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e")
        label1 = customtkinter.CTkLabel(frame, text="LIION ASSIST", height=14,
                                        font=customtkinter.CTkFont(family="Inter", size=20),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame, text="STAY FOCUSED ON THE ROAD", height=10,
                                        font=customtkinter.CTkFont(family="Inter", size=10), text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

        #
        self.bouton_suivant = customtkinter.CTkButton(self, text="Suivant", width=50, height=20,
                                                      command=self.fenetre_suivante1)
        self.bouton_suivant.grid(row=2, column=1)

    def effacer(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        return self

    def fenetre_suivante1(self):
        self.effacer()
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        text_instruction = """Pour connecter votre téléphone à votre console multimedia, suivez les étapes suivantes ci dessous: 

                1.  Ouvrez l'application LIION ASSIST sur votre smartphone; Bien vouloir la télécharger 
                     sur le Playstore si elle n'est pas encore installée ;
                2.  Autorisez l'accès à l'appareil photo, au WIFI, et au micro puis, cliquer sur le bouton
                     CONNECTER pour établir la connection ;
                3.  Positionnez votre téléphone face à la console pour scanner le code QR ci dessus ;
                4.  Une fois connecté, vous pouvez à présent jouir des fonctionnalités offertes par 
                     LIION ASSIST."""

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=150,
            border=1
        )
        code = "ce_texte_est_un_code"
        qr.add_data(code)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_qr.save("images/qrcode.png")

        #
        frame = customtkinter.CTkFrame(self, fg_color=self.default_bg_color)
        frame.grid(row=0, column=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=0)
        frame.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(64, 82))
        photo = customtkinter.CTkLabel(frame, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e", ipadx=15)
        label1 = customtkinter.CTkLabel(frame, text="LIION ASSIST", height=14,
                                        font=customtkinter.CTkFont(family="Inter", size=12),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame, text="STAY FOCUSED ON THE ROAD", height=10,
                                        font=customtkinter.CTkFont(family="Inter", size=7), text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

        #
        img_qrcode = customtkinter.CTkImage(light_image=PIL.Image.open("images/qrcode.png"), size=(150, 150))
        qrframe = customtkinter.CTkLabel(self, width=150, height=150, image=img_qrcode, text="")
        qrframe.grid(row=1, column=1)
        label3 = customtkinter.CTkLabel(self, text=text_instruction, width=150,
                                        font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                        text_color=self.default_text_color, justify=customtkinter.LEFT)
        label3.grid(row=3, column=1, pady=30)

        #
        bouton_suivant1 = customtkinter.CTkButton(self, text="Suivant", width=50, height=20,
                                                  command=self.fenetre_suivante2)
        bouton_suivant1.grid(row=4, column=1)

    def fenetre_suivante2(self):
        self.effacer()
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
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=self.home_icon_dimen, fg_color=self.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(self.home_icon_dimen,
                                                                                               self.home_icon_dimen))
        image_home = customtkinter.CTkButton(home_frame, width=self.home_icon_dimen,
                                             height=self.home_icon_dimen,
                                             image=img_home, text="", command=self.quit,
                                             fg_color=self.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frametest3 = customtkinter.CTkFrame(self, fg_color=self.default_bg_color, width=100)
        frametest3.grid(row=1, column=2)
        frametest3.grid_rowconfigure(0, weight=1)
        frametest3.grid_rowconfigure(1, weight=0)
        frametest3.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(92, 117))
        photo = customtkinter.CTkLabel(frametest3, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e")
        label1 = customtkinter.CTkLabel(frametest3, text="LIION ASSIST", height=14,
                                        font=customtkinter.CTkFont(family="Inter", size=15),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frametest3, text="STAY FOCUSED ON THE ROAD", height=10,
                                        font=customtkinter.CTkFont(family="Inter", size=7), text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=self.default_bar_color, width=self.home_icon_dimen,
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=self.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter", size=self.default_text_size + 8),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=self.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter", size=self.default_text_size - 2),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        # cadre des icones
        barnav_frame = customtkinter.CTkFrame(self, fg_color=self.default_bg_color)
        barnav_frame.grid(row=2, column=1, rowspan=1, columnspan=3)

        #
        Icon.nombre_cree = 0
        phone_icon = Icon(barnav_frame, "Telephone", self.default_text_size, "images/phone.png",
                          self.default_icon_dimen, 0, 0)
        phone_icon.creer()
        gps_icon = Icon(barnav_frame, "GPS", self.default_text_size, "images/gps.png", self.default_icon_dimen, 0,
                        1)
        gps_icon.creer()
        musique_icon = Icon(barnav_frame, "Music", self.default_text_size, "images/music.png",
                            self.default_icon_dimen, 0, 2)
        musique_icon.creer()
        video_icon = Icon(barnav_frame, "Videos", self.default_text_size, "images/video.png",
                          self.default_icon_dimen, 0, 3)
        video_icon.creer()
        settings_icon = Icon(barnav_frame, "Parametres", self.default_text_size, "images/settings.png",
                             self.default_icon_dimen, 0, 4)
        settings_icon.creer()
        sms_icon = Icon(barnav_frame, "Messages", self.default_text_size, "images/sms.png",
                        self.default_icon_dimen, 0, 5)
        sms_icon.creer()


class Icon:
    nombre_cree = 0

    def __init__(self, parent, nom, police, source_image, taille, xligne, ycolone):
        Icon.nombre_cree += 1
        self.parent = parent
        self.nom = nom
        self.police = police
        self.source_image = source_image
        self.taille = taille
        self.xligne = xligne
        self.ycolone = ycolone

    def creer(self):
        frame = customtkinter.CTkFrame(self.parent, width=self.taille, height=self.taille, fg_color="#0F0332")
        frame.grid(row=self.xligne, column=self.ycolone, padx=5)
        frame.grid_rowconfigure(0)
        frame.grid_rowconfigure(1)
        img = customtkinter.CTkImage(light_image=PIL.Image.open(self.source_image),
                                     size=(self.taille, self.taille))
        program = """image = customtkinter.CTkButton(frame, width=self.taille, fg_color="#0F0332", height=self.taille, image=img, text="",
                                        command= self.fenetreIcon"""+str(Icon.nombre_cree)+") \nimage.grid(row=0, column=0)"
        exec(program)
        label = customtkinter.CTkLabel(frame, text=self.nom, fg_color="#0F0332",
                                       font=customtkinter.CTkFont(family="Inter", size=self.police),
                                       text_color="#FFFFFF")
        label.grid(row=1, column=0)

    def fenetreIcon1(self):
        app.fenetre_suivante1()
    def fenetreIcon2(self):
        app.fenetre_suivante1()
    def fenetreIcon3(self):
        app.fenetre_suivante1()
    def fenetreIcon4(self):
        app.fenetre_suivante1()
    def fenetreIcon5(self):
        app.fenetre_suivante1()
    def fenetreIcon6(self):
        app.fenetre_suivante1()


if __name__ == "__main__":
    app = App()
    app.mainloop()

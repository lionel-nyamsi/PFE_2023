import customtkinter
import PIL.Image
import qrcode


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # app configuration
        self.geometry("835.8x583.8")
        self.title("LIION ASSIST")
        self.minsize(835.8, 583.8)
        self.maxsize(835.8, 583.8)
        self.configure(fg_color="#0F0332")

        # activities(pages) configuration
        self.default_text_color="#C9C5C5"
        self.default_text_size=12
        self.home_icon_dimen=50
        self.default_icon_dimen=70
        self.phone_sms_icon_dimen=self.default_icon_dimen
        self.default_icon_frame_width=self.default_icon_dimen+15
        self.default_icon_frame_height=self.default_icon_dimen+25

        # create 2x2 grid system
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(128.1, 163.8))
        self.frame = customtkinter.CTkFrame(self, width=140, height=220, fg_color="#0F0332")
        self.frame.grid(row=1, column=1)
        self.photo = customtkinter.CTkLabel(self.frame, image=logo, text="")
        self.photo.place(x=20, y=0)
        self.label1 = customtkinter.CTkLabel(self.frame, text="LIION ASSIST",
                                             font=customtkinter.CTkFont(family="Inter", size=20), text_color="#FFFFFF")
        self.label1.place(x=0, y=170)
        self.label2 = customtkinter.CTkLabel(self.frame, text="STAY FOCUSED ON THE ROAD",
                                             font=customtkinter.CTkFont(family="Inter", size=9), text_color="#EAA623",
                                             anchor="n", justify="center")
        self.label2.place(x=0, y=195)
        self.bouton_suivant = customtkinter.CTkButton(self, text="Suivant", width=50, height=20,
                                                      command=self.fenetre_suivante1)
        self.bouton_suivant.grid(row=2, column=1)

    def effacer(self):
        for widget in self.winfo_children():
            widget.grid_forget()

    def fenetre_suivante1(self):
        # self.bouton_suivant.grid_forget()
        # self.frame.grid_forget()
        self.effacer()
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

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

        logo2 = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(64.05, 81.9))
        self.frame2 = customtkinter.CTkFrame(self, width=70, height=110, fg_color="#0F0332")
        self.frame2.grid(row=0, column=1)
        self.photo2 = customtkinter.CTkLabel(self.frame2, image=logo2, text="")
        self.photo2.place(x=10, y=0)
        self.label21 = customtkinter.CTkLabel(self.frame2, text="LIION ASSIST",
                                              font=customtkinter.CTkFont(family="Inter", size=10),
                                              text_color="#FFFFFF", anchor="n")
        self.label21.place(x=2.5, y=85)
        self.label22 = customtkinter.CTkLabel(self.frame2, text="STAY FOCUSED ON THE ROAD",
                                              font=customtkinter.CTkFont(family="Inter", size=5), text_color="#EAA623",
                                              anchor="nw", justify="center")
        self.label22.place(x=0, y=97.5)
        img_qrcode = customtkinter.CTkImage(light_image=PIL.Image.open("images/qrcode.png"), size=(150, 150))
        self.qrframe = customtkinter.CTkLabel(self, width=150, height=150, image=img_qrcode, text="")
        self.qrframe.grid(row=1, column=1)
        self.label3 = customtkinter.CTkLabel(self, text=text_instruction, width=150,
                                             font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                             text_color=self.default_text_color, justify=customtkinter.LEFT)
        self.label3.grid(row=3, column=1, pady=30)

        self.bouton_suivant1 = customtkinter.CTkButton(self, text="Suivant", width=50, height=20,
                                                       command=self.fenetre_suivante2)
        self.bouton_suivant1.grid(row=4, column=1)

    def fenetre_suivante2(self):
        self.effacer()
        self.bouton_suivant1.grid_forget()
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=0)

        # cadre des icones
        self.barnav_frame = customtkinter.CTkFrame(self, width=self.default_icon_frame_width*7, # car, il y'a 7 icones
                                                   height=self.default_icon_frame_height+50, fg_color="#FFFFFF")
        self.barnav_frame.grid_rowconfigure(0, weight=1)
        self.barnav_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.barnav_frame.grid(row=3, column=1, pady=30, columnspan=2)

        #
        self.phone_frame = customtkinter.CTkFrame(self.barnav_frame, width=self.default_icon_frame_width, height=self.default_icon_frame_height, fg_color="#0F0332")
        self.phone_frame.grid(row=0, column=1, padx=5)
        img_phone = customtkinter.CTkImage(light_image=PIL.Image.open("images/phone.png"), size=(self.phone_sms_icon_dimen, self.phone_sms_icon_dimen))
        self.image_phone = customtkinter.CTkButton(self.phone_frame, width=self.default_icon_dimen, height=self.default_icon_dimen,
                                                   image=img_phone, text="", command=self.fenetre_suivante1, fg_color="#0F0332")
        self.image_phone.place(x=0, y=0)
        self.label_phone = customtkinter.CTkLabel(self.phone_frame, text="Telephone",
                                                  font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                                  text_color=self.default_text_color, anchor="n")
        self.label_phone.place(x=7, y=self.phone_sms_icon_dimen+self.default_text_size)

        #
        self.gps_frame = customtkinter.CTkFrame(self.barnav_frame, width=self.default_icon_frame_width,
                                                height=self.default_icon_frame_height, fg_color="#0F0332")
        self.gps_frame.grid(row=0, column=2, padx=5)
        img_gps = customtkinter.CTkImage(light_image=PIL.Image.open("images/gps.png"), size=(self.default_icon_dimen, self.default_icon_dimen))
        self.image_gps = customtkinter.CTkButton(self.gps_frame, width=self.default_icon_dimen, height=self.default_icon_dimen,
                                                 image=img_gps, text="", command=self.fenetre_suivante1, fg_color="#0F0332")
        self.image_gps.place(x=0, y=0)
        self.label_gps = customtkinter.CTkLabel(self.gps_frame, text="GPS",
                                                font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                                text_color=self.default_text_color, anchor="n")
        self.label_gps.place(x=20, y=self.default_icon_dimen+self.default_text_size)

        #
        self.music_frame = customtkinter.CTkFrame(self.barnav_frame, width=self.default_icon_frame_width, height=self.default_icon_frame_height, fg_color="#0F0332")
        self.music_frame.grid(row=0, column=3, padx=5)
        img_music = customtkinter.CTkImage(light_image=PIL.Image.open("images/music.png"), size=(self.default_icon_dimen, self.default_icon_dimen))
        self.image_music = customtkinter.CTkButton(self.music_frame, width=50, height=50, image=img_music, text="",
                                                   command=self.fenetre_suivante1, fg_color="#0F0332")
        self.image_music.place(x=0, y=0)
        self.label_music = customtkinter.CTkLabel(self.music_frame, text="Musiques",
                                                  font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                                  text_color=self.default_text_color, anchor="n")
        self.label_music.place(x=7, y=self.default_icon_dimen+self.default_text_size)

        #
        self.video_frame = customtkinter.CTkFrame(self.barnav_frame, width=self.default_icon_frame_width, height=self.default_icon_frame_height, fg_color="#0F0332")
        self.video_frame.grid(row=0, column=4, padx=5)
        img_video = customtkinter.CTkImage(light_image=PIL.Image.open("images/video.png"), size=(self.default_icon_dimen,self.default_icon_dimen))
        self.image_video = customtkinter.CTkButton(self.video_frame, width=self.default_icon_dimen, height=self.default_icon_dimen,
                                                   image=img_video, text="", command=self.fenetre_suivante1, fg_color="#0F0332")
        self.image_video.place(x=0, y=0)
        self.label_video = customtkinter.CTkLabel(self.video_frame, text="Videos",
                                                  font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                                  text_color=self.default_text_color, anchor="n")
        self.label_video.place(x=14, y=self.default_icon_dimen+self.default_text_size)

        #
        self.settings_frame = customtkinter.CTkFrame(self.barnav_frame, width=self.default_icon_frame_width, height=self.default_icon_frame_height, fg_color="#0F0332")
        self.settings_frame.grid(row=0, column=5, padx=5)
        img_settings = customtkinter.CTkImage(light_image=PIL.Image.open("images/settings.png"), size=(self.default_icon_dimen, self.default_icon_dimen+5))
        self.image_settings = customtkinter.CTkButton(self.settings_frame, width=self.phone_sms_icon_dimen, height=self.phone_sms_icon_dimen, image=img_settings,
                                                      text="", command=self.fenetre_suivante1, fg_color="#0F0332")
        self.image_settings.place(x=0, y=0)
        self.label_settings = customtkinter.CTkLabel(self.settings_frame, text="Parametres",
                                                     font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                                     text_color=self.default_text_color, anchor="n")
        self.label_settings.place(x=0, y=self.default_icon_dimen+self.default_text_size)

        #
        self.sms_frame = customtkinter.CTkFrame(self.barnav_frame, width=self.default_icon_frame_width, height=self.default_icon_frame_height, fg_color="#0F0332")
        self.sms_frame.grid(row=0, column=6, padx=5)
        img_sms = customtkinter.CTkImage(light_image=PIL.Image.open("images/sms.png"), size=(self.phone_sms_icon_dimen, self.phone_sms_icon_dimen))
        self.image_sms = customtkinter.CTkButton(self.sms_frame, width=self.default_icon_dimen, height=self.default_icon_dimen, image=img_sms, text="",
                                                 command=self.fenetre_suivante1, fg_color="#0F0332")
        self.image_sms.place(x=0, y=0)
        self.label_sms = customtkinter.CTkLabel(self.sms_frame, text="Messages",
                                                font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                                text_color=self.default_text_color, anchor="n")
        self.label_sms.place(x=5, y=self.phone_sms_icon_dimen+self.default_text_size)

        #
        self.car_frame = customtkinter.CTkFrame(self.barnav_frame, width=self.default_icon_frame_width, height=self.default_icon_frame_height, fg_color="#0F0332")
        self.car_frame.grid(row=0, column=7, padx=5)
        img_car = customtkinter.CTkImage(light_image=PIL.Image.open("images/car.png"), size=(self.default_icon_dimen, self.default_icon_dimen))
        self.image_car = customtkinter.CTkButton(self.car_frame, width=self.default_icon_dimen, height=self.default_icon_dimen, image=img_car, text="",
                                                 command=self.fenetre_suivante1, fg_color="#0F0332")
        self.image_car.place(x=0, y=0)
        self.label_car = customtkinter.CTkLabel(self.car_frame, text="Voiture",
                                                font=customtkinter.CTkFont(family="Inter", size=self.default_text_size),
                                                text_color=self.default_text_color, anchor="n")
        self.label_car.place(x=15, y=self.default_icon_dimen+self.default_text_size)

        # cadre barre verticale de taches
        self.barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        self.barinf_cadre.grid(row=0, column=0, rowspan=3)

        self.barinf_frame = customtkinter.CTkFrame(self.barinf_cadre, width=self.home_icon_dimen+30, height=583.8,
                                                   corner_radius=0, fg_color="#49585B")
        self.barinf_frame.grid(row=0, column=0)
        self.barinf_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.barinf_frame.grid_columnconfigure(0, weight=1)

        #
        self.home_frame = customtkinter.CTkFrame(self.barinf_frame, width=self.home_icon_dimen,
                                                 height=self.home_icon_dimen, fg_color="#59585B")
        self.home_frame.grid(row=0, column=0)


        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(self.home_icon_dimen,
                                                                                               self.home_icon_dimen))
        self.image_home = customtkinter.CTkButton(self.home_frame, width=self.home_icon_dimen, height=self.home_icon_dimen,
                                                  image=img_home, text="", command=self.quit, fg_color="#59585B")
        self.image_home.grid(row=10, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()

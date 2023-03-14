import customtkinter
import PIL.Image
import qrcode
import home_page


class ConnectionPage(customtkinter.CTkFrame):

    def __init__(self, parent, app):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=app.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        text_instruction = """Pour connecter votre téléphone à votre console multimedia, suivez les étapes suivantes 
        ci dessous:

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
            box_size=150 * app.scale,
            border=1
        )
        code = "ce_texte_est_un_code"
        qr.add_data(code)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_qr.save("images/qrcode.png")

        #
        frame = customtkinter.CTkFrame(self, fg_color=app.default_bg_color)
        frame.grid(row=0, column=1, pady=20)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=0)
        frame.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"),
                                      size=(int(64 * app.scale), int(82 * app.scale)))
        photo = customtkinter.CTkLabel(frame, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e", ipadx=int(17 / app.scale))
        label1 = customtkinter.CTkLabel(frame, text="LIION ASSIST", height=14,
                                        font=customtkinter.CTkFont(family="Inter", size=12),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame, text="STAY FOCUSED ON THE ROAD", height=10,
                                        font=customtkinter.CTkFont(family="Inter", size=7), text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

        #
        img_qrcode = customtkinter.CTkImage(light_image=PIL.Image.open("images/qrcode.png"),
                                            size=(int(150 * app.scale), int(150 * app.scale)))
        qrframe = customtkinter.CTkLabel(self, width=int(150 * app.scale), height=int(150 * app.scale),
                                         image=img_qrcode, text="")
        qrframe.grid(row=1, column=1)
        label3 = customtkinter.CTkLabel(self, text=text_instruction, width=150,
                                        font=customtkinter.CTkFont(family="Inter", size=int(app.default_text_size)),
                                        text_color=app.default_text_color, justify=customtkinter.LEFT)
        label3.grid(row=3, column=1, pady=30)

        #
        bouton_suivant1 = customtkinter.CTkButton(self, text="Suivant", width=50, height=20,
                                                  command=lambda: app.show_frame(home_page.HomePage))
        bouton_suivant1.grid(row=4, column=1)

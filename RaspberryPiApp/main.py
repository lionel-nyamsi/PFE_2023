import customtkinter
import PIL.Image
import qrcode


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("835.8x583.8")
        self.title("Liion")
        self.minsize(835.8, 583.8)
        self.maxsize(835.8, 583.8)
        self.configure(fg_color="#0F0332")

        # create 2x2 grid system
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(128.1, 163.8))
        self.frame = customtkinter.CTkFrame(self, width=140, height=220, fg_color="#0F0332")
        self.frame.grid(row=1, column=1)
        self.photo = customtkinter.CTkLabel(self.frame, image=logo, text="")
        self.photo.place(x=20, y=0)
        self.label1 = customtkinter.CTkLabel(self.frame, text="LIION ASSIST",
                                             font=customtkinter.CTkFont(family="Inter", size=20))
        self.label1.place(x=5, y=170)
        self.label2 = customtkinter.CTkLabel(self.frame, text="STAY FOCUSED ON THE ROAD",
                                             font=customtkinter.CTkFont(family="Inter", size=9), text_color="#EAA623",
                                             anchor="n", justify="center")
        self.label2.place(x=0, y=195)
        self.bouton_suivant = customtkinter.CTkButton(self, text="Suivant", width=50, height=20, command=self.fenetre_suivante1)
        self.bouton_suivant.grid(row=2, column=1)

    def fenetre_suivante1(self):
        self.bouton_suivant.grid_forget()
        self.frame.grid_forget()
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        text_instruction = """Pour connecter votre téléphone à votre console multimedia, suivez les étapes suivantes ci dessous: 
        
        1.  Ouvrir l'application LIION ASSIST sur votre smartphone; Bien vouloir la télécharger 
             sur le Playstore si elle n'est pas encore installée;
        2.  Autoriser l'accès à l'appareil photo, au WIFI, et au micro puis, cliquer sur le bouton
             CONNECTER pour établir la connection;
        3.  Scanner le code QR ci dessus;
        4.  Une fois connecté, vous pouvez à présent jouir des fonctionnalités offertes par 
             LIION ASSIST."""

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=150,
            border=1
        )
        code = "cetexteestuncode"
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
                                             font=customtkinter.CTkFont(family="Inter", size=10), anchor="n")
        self.label21.place(x=2.5, y=85)
        self.label22 = customtkinter.CTkLabel(self.frame2, text="STAY FOCUSED ON THE ROAD",
                                             font=customtkinter.CTkFont(family="Inter", size=5), text_color="#EAA623",
                                             anchor="nw", justify="center")
        self.label22.place(x=0, y=97.5)
        img_qrcode = customtkinter.CTkImage(light_image=PIL.Image.open("images/qrcode.png"), size=(150, 150))
        self.qrframe = customtkinter.CTkLabel(self, width=150, height=150, image=img_qrcode, text="")
        self.qrframe.grid(row=1, column=1)
        self.label3 = customtkinter.CTkLabel(self, text=text_instruction, width=150,
                                             font=customtkinter.CTkFont(family="Inter", size=12), justify=customtkinter.LEFT)
        self.label3.grid(row=3, column=1, pady=30)


if __name__ == "__main__":
    app = App()
    app.mainloop()

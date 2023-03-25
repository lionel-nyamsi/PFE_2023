import customtkinter
import PIL.Image
import home_page
import contacts


class PageIcon1(customtkinter.CTkFrame):  # phone page class
    color = {
        "white": '#FFFFFF',
        "black": '#000000',
        "gray": '#C7C7C7',
        "light-gray": '#D9D9D9'
    }

    icon_nav_dimen = 40
    text_size_icon_nav = 12
    default_margin = 15
    contact_name_text_size = 18

    def __init__(self, parent, app):
        customtkinter.CTkFrame.__init__(self, parent)

        self.app = app
        self.icon_dimen = app.default_icon_dimen
        self.bg_color = app.default_bg_color

        self.configure(fg_color=app.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color=app.default_bar_color)
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
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="\n15:45", fg_color=app.default_bar_color,
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
        frame_phone = customtkinter.CTkFrame(barinf_cadre, width=int(app.home_icon_dimen),
                                             fg_color=app.default_bar_color)
        frame_phone.grid(row=1, column=0, pady=20, sticky='esw')
        frame_phone.grid_rowconfigure(0, weight=1)
        img_phone = customtkinter.CTkImage(light_image=PIL.Image.open("images/phone.png"),
                                           size=(int(app.home_icon_dimen), int(app.home_icon_dimen)))
        image_phone = customtkinter.CTkButton(frame_phone, width=int(app.home_icon_dimen),
                                              height=int(app.home_icon_dimen), image=img_phone, text="",
                                              command=lambda: app.show_frame(home_page.HomePage),
                                              fg_color=app.default_bar_color)
        image_phone.grid(row=0, column=0)

        # Création du box Telephone proprement dit
        box_phone = customtkinter.CTkFrame(self, corner_radius=0)
        box_phone.grid(row=0, column=1, rowspan=3, columnspan=1, sticky='nesw')
        box_phone.grid_rowconfigure(0, weight=0)
        box_phone.grid_rowconfigure(1, weight=1)
        box_phone.grid_rowconfigure(2, weight=0)
        box_phone.grid_columnconfigure(0, weight=1, uniform='same_group')
        box_phone.grid_columnconfigure(1, weight=1, uniform='same_group')
        box_phone.grid_columnconfigure(2, weight=1, uniform='same_group')
        box_phone.grid_columnconfigure(3, weight=1, uniform='same_group')

        # Barre de titre
        title_bar = customtkinter.CTkFrame(box_phone, corner_radius=0, fg_color=self.color["gray"])
        title_bar.grid(row=0, column=0, rowspan=1, columnspan=4, sticky='nesw')
        title_bar.columnconfigure(0, weight=0)
        title_bar.columnconfigure(1, weight=1)
        title_bar.columnconfigure(2, weight=0)

        logo_frame = customtkinter.CTkFrame(title_bar, corner_radius=0, fg_color=self.color["gray"])
        logo_frame.grid(row=0, column=0, rowspan=1, columnspan=1, sticky='')
        logo_img = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"),
                                          dark_image=PIL.Image.open("images/logo.png"),
                                          size=(15, 20))
        logo = customtkinter.CTkLabel(logo_frame, image=logo_img, text="", fg_color=self.color["gray"])
        logo.grid(row=0, column=0, sticky='n', padx=5)

        name = customtkinter.CTkLabel(title_bar, text="Téléphone", fg_color=self.color["gray"],
                                      font=customtkinter.CTkFont(family="Inter", size=17, weight="bold"),
                                      text_color="#000000")
        name.grid(row=0, column=1, sticky='w')

        close_img = customtkinter.CTkImage(light_image=PIL.Image.open("images/close.png"),
                                           dark_image=PIL.Image.open("images/close.png"),
                                           size=(20, 20))
        close_btn = customtkinter.CTkButton(title_bar, image=close_img, text="", fg_color=self.color["gray"],
                                            height=20, width=20,
                                            command=lambda: app.show_frame(home_page.HomePage))
        close_btn.grid(row=0, column=2, sticky='e')

        # Barre de navigation
        self.draw_contents(box_phone, "Récents")
        self.draw_nav_bar(box_phone, "Récents")

    def draw_nav_bar(self, parent, icon_name):
        nav_bar = customtkinter.CTkFrame(parent, corner_radius=0, height=self.app.default_icon_dimen,
                                         fg_color=self.color["light-gray"])
        nav_bar.grid(row=2, column=0, rowspan=1, columnspan=2, sticky='nesw')
        nav_bar.grid_rowconfigure(0, weight=1)
        nav_bar.grid_columnconfigure(0, weight=1)
        nav_bar.grid_columnconfigure(1, weight=1)
        nav_bar.grid_columnconfigure(2, weight=1)

        if icon_name == "Contacts":
            IconNav(nav_bar, "Contacts", "images/contact.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 0, True, parent, self.draw_nav_bar,
                    self.draw_contents)
            IconNav(nav_bar, "Récents", "images/recents.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 1, False, parent, self.draw_nav_bar,
                    self.draw_contents)
            IconNav(nav_bar, "Favoris", "images/favoris.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 2, False, parent, self.draw_nav_bar,
                    self.draw_contents)
        elif icon_name == "Récents":
            IconNav(nav_bar, "Contacts", "images/contact.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 0, False, parent, self.draw_nav_bar,
                    self.draw_contents)
            IconNav(nav_bar, "Récents", "images/recents.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 1, True, parent, self.draw_nav_bar,
                    self.draw_contents)
            IconNav(nav_bar, "Favoris", "images/favoris.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 2, False, parent, self.draw_nav_bar,
                    self.draw_contents)
        elif icon_name == "Favoris":
            IconNav(nav_bar, "Contacts", "images/contact.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 0, False, parent, self.draw_nav_bar,
                    self.draw_contents)
            IconNav(nav_bar, "Récents", "images/recents.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 1, False, parent, self.draw_nav_bar,
                    self.draw_contents)
            IconNav(nav_bar, "Favoris", "images/favoris.png", self.icon_nav_dimen, "Inter", self.text_size_icon_nav,
                    self.color["light-gray"], self.color["black"], 0, 2, True, parent, self.draw_nav_bar,
                    self.draw_contents)
        else:
            print("Une erreur est survenue lors de la géneration de la barre de navigation.")

    def draw_contents(self, parent, icon_name):  # dessine à la fois le left_content et le right_content
        # Left_content
        global content, frame_label_text
        left_content = customtkinter.CTkFrame(parent, corner_radius=0, fg_color=self.color["white"])
        left_content.grid(row=1, column=0, rowspan=1, columnspan=2, sticky='nesw')
        left_content.rowconfigure(0, weight=0)
        left_content.rowconfigure(1, weight=0)
        left_content.rowconfigure(2, weight=1)
        left_content.columnconfigure(0, weight=1, uniform='same_group')

        right_content = customtkinter.CTkFrame(parent, corner_radius=0, fg_color=self.app.default_bg_color)
        right_content.grid(row=1, column=2, rowspan=2, columnspan=2, sticky='nesw')
        right_content.rowconfigure(0, weight=1)
        right_content.columnconfigure(0, weight=1)

        if icon_name == "Contacts":
            frame_label_text = "Contacts"
            content = self.load_contacts(left_content, right_content)
        elif icon_name == "Récents":
            frame_label_text = "Journal des appels"
            content = self.load_recents(left_content, right_content)
        elif icon_name == "Favoris":
            frame_label_text = "Mes favoris"
            content = self.load_favoris(left_content, right_content)
        else:
            print("Erreur sur le nom du fragment.")

        research_bar = customtkinter.CTkEntry(left_content, corner_radius=10,
                                              placeholder_text="Rechercher des contacts",
                                              fg_color=self.color["light-gray"], text_color=self.app.default_text_color,
                                              font=customtkinter.CTkFont(family="Inter",
                                                                         size=int(self.app.default_text_size)))
        research_bar.grid(row=0, column=0, padx=self.default_margin, pady=self.default_margin, sticky='ew')

        frame_label = customtkinter.CTkLabel(left_content, text=frame_label_text, text_color=self.color["black"],
                                             font=customtkinter.CTkFont(family="Inter",
                                                                        size=int(self.app.title_text_size),
                                                                        weight='bold'))
        frame_label.grid(row=1, column=0, padx=self.default_margin, sticky='w')

        content.grid(row=2, column=0, padx=self.default_margin, sticky='nesw')

    def load_contacts(self, left_content, right_content):

        box = customtkinter.CTkFrame(left_content, corner_radius=0, fg_color=self.color["white"])
        box.columnconfigure(0, weight=1)

        contact_1 = contacts.Contact(self, box, right_content, "Armel", "699090806", self.color["light-gray"])
        contact_2 = contacts.Contact(self, box, right_content, "Betani", "699090806", self.color["light-gray"])
        contact_3 = contacts.Contact(self, box, right_content, "Carole", "699090806", self.color["light-gray"])

        contacts_list = list()
        contacts_list.append(contact_1)
        contacts_list.append(contact_2)
        contacts_list.append(contact_3)

        i = 0
        while i < len(contacts_list):
            box.rowconfigure(i, weight=0)
            i += 1

        for i, contact in enumerate(contacts_list):
            contact_frame = contact.create_contact_frame()
            contact_frame.grid(row=i, column=0, pady=5, sticky='nesw')

        return box

    def load_recents(self, left_content, right_content):

        content = customtkinter.CTkFrame(left_content, corner_radius=0, fg_color=self.color["white"])
        content.columnconfigure(0, weight=1)

        return content

    def load_favoris(self, left_content, right_content):

        content = customtkinter.CTkFrame(left_content, corner_radius=0, fg_color=self.color["white"])
        content.columnconfigure(0, weight=1)

        return content


class IconNav(customtkinter.CTkButton):
    def __init__(self, parent, name, img_src, dimen, police, police_size, bg_color, text_color, row, column,
                 is_turned_on, gp, func_nav, func_main):
        self.parent = parent
        self.name = name
        self.img_src = img_src
        self.dimen = int(dimen)
        self.police = police
        self.police_size = int(police_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.row = int(row)
        self.column = int(column)
        self.is_turned_on = bool(is_turned_on)
        self.gp = gp  # gp est le widget parent du widget parend de cette icone. (c'est-à-dire box_phone)
        self.func_nav = func_nav
        self.func_main = func_main

        self.createIcon()

    def createIcon(self):
        if self.is_turned_on:
            i = 0
            lenght = len(self.img_src)
            lenght -= 4  # car '.png' compte 4 caractères
            image_source = ""
            while i < lenght:
                image_source += self.img_src[i]
                i += 1
            image_source += "_on.png"
            self.img_src = image_source

        icon_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color=self.bg_color)
        icon_frame.grid(row=self.row, column=self.column)
        icon_frame.grid_rowconfigure(0, weight=1)
        icon_frame.grid_rowconfigure(1, weight=0)
        icon_frame.grid_columnconfigure(0, weight=1)

        img = customtkinter.CTkImage(light_image=PIL.Image.open(self.img_src),
                                     dark_image=PIL.Image.open(self.img_src),
                                     size=(self.dimen, self.dimen))
        icon_btn = customtkinter.CTkButton(icon_frame, image=img, text="", fg_color=self.bg_color,
                                           width=self.dimen, height=self.dimen, command=self.execute)
        icon_btn.grid(row=0, column=0, sticky='s')

        icon_name = customtkinter.CTkLabel(icon_frame, text=self.name, fg_color=self.bg_color,
                                           font=customtkinter.CTkFont(self.police, size=self.police_size),
                                           text_color=self.text_color)
        icon_name.grid(row=1, column=0)

    def execute(self):
        i = 0
        lenght = len(self.img_src)
        lenght -= 4  # car '.png' compte 4 caractères
        image_source = ""
        while i < lenght:
            image_source += self.img_src[i]
            i += 1
        if image_source[lenght - 2] == 'o' and image_source[lenght - 1] == 'n':
            '''i = 0
            image_source2 = ""
            while i < len(image_source) - 3:
                image_source2 += image_source[i]
                i += 1
            self.img_src = image_source2 + ".png"
            self.createIcon()'''
        else:
            image_source += "_on.png"
            self.img_src = image_source
            self.createIcon()
        self.func_nav(self.gp, self.name)
        self.func_main(self.gp, self.name)

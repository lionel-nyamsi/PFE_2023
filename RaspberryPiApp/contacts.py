import customtkinter
import PIL


class Contact:
    colors = {
        "white": '#FFFFFF',
        "black": '#000000',
        "gray": '#C7C7C7',
        "light-gray": '#D9D9D9'
    }

    def __init__(self, parent, content_left, content_right, first_name, number1, color, last_name='', number2=''):
        self.contact_name = None
        self.parent = parent
        self.content_left = content_left
        self.content_right = content_right
        self.first_name = str(first_name)
        self.last_name = last_name
        self.number_1 = str(number1)
        self.number_2 = number2
        self.bg_color = color
        self.color = "#1E7910"

    def create_contact_frame(self):
        contact_frame = customtkinter.CTkButton(self.content_left, corner_radius=20, fg_color=self.bg_color, text='',
                                                command=self.display_contact)
        contact_frame.rowconfigure(0, weight=1)
        contact_frame.columnconfigure(0, weight=0)
        contact_frame.columnconfigure(1, weight=1)

        raduis = 40
        picture = customtkinter.CTkFrame(contact_frame, fg_color=self.color, height=raduis, width=raduis,
                                         corner_radius=raduis // 2)
        text_picture = customtkinter.CTkLabel(contact_frame, fg_color=self.color,
                                              text_color=self.colors["white"],
                                              text=self.first_name[0].upper(),
                                              font=customtkinter.CTkFont(family="Inter", size=25, weight="bold"))
        picture.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        text_picture.grid(row=0, column=0, padx=6 + raduis / 4, sticky='w')

        self.contact_name = customtkinter.CTkLabel(contact_frame, text=self.first_name + " " + self.last_name,
                                                   font=customtkinter.CTkFont(family="Inter", size=18))
        self.contact_name.grid(row=0, column=1, padx=5, sticky='w')

        return contact_frame

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

    def display_contact(self):

        tools_bar_bg_color = self.parent.bg_color
        default_icon_dimen = self.parent.icon_dimen
        default_margin = 5
        icon_dimen = 20

        contact_window = customtkinter.CTkFrame(self.content_right, corner_radius=0, fg_color=tools_bar_bg_color,
                                                width=(836 - default_icon_dimen - 10) // 2)
        contact_window.grid(row=0, column=0, sticky='nesw')
        contact_window.rowconfigure(0, weight=0)
        contact_window.rowconfigure(1, weight=0)
        contact_window.rowconfigure(2, weight=0)
        contact_window.rowconfigure(3, weight=0)
        contact_window.columnconfigure(0, weight=1)

        # Barre d'outils
        tools_bar = customtkinter.CTkFrame(contact_window, corner_radius=0, fg_color=tools_bar_bg_color)
        tools_bar.grid(row=0, column=0, sticky='nesw')
        tools_bar.rowconfigure(0, weight=1)
        tools_bar.columnconfigure(0, weight=1)
        tools_bar.columnconfigure(1, weight=0)
        tools_bar.columnconfigure(2, weight=0)

        image_favorite = customtkinter.CTkImage(light_image=PIL.Image.open("images/favoris.png"),
                                                dark_image=PIL.Image.open("images/favoris.png"),
                                                size=(icon_dimen, icon_dimen))
        favorite = customtkinter.CTkButton(tools_bar, corner_radius=0, width=icon_dimen, height=icon_dimen, text='',
                                           image=image_favorite, fg_color=tools_bar_bg_color)
        favorite.grid(row=0, column=0, sticky='e', padx=default_margin, pady=(default_margin, 0))

        image_modify = customtkinter.CTkImage(light_image=PIL.Image.open("images/modify.png"),
                                              dark_image=PIL.Image.open("images/modify.png"),
                                              size=(icon_dimen, icon_dimen))
        modify = customtkinter.CTkButton(tools_bar, corner_radius=0, width=icon_dimen, height=icon_dimen, text='',
                                         image=image_modify, fg_color=tools_bar_bg_color)
        modify.grid(row=0, column=1, sticky='e', padx=default_margin, pady=(default_margin, 0))

        image_delete = customtkinter.CTkImage(light_image=PIL.Image.open("images/delete_contact.png"),
                                              dark_image=PIL.Image.open("images/delete_contact.png"),
                                              size=(icon_dimen, icon_dimen))
        delete = customtkinter.CTkButton(tools_bar, corner_radius=0, width=icon_dimen, height=icon_dimen, text='',
                                         image=image_delete, fg_color=tools_bar_bg_color)
        delete.grid(row=0, column=2, sticky='e', padx=default_margin, pady=(default_margin, 0))

        # content
        picture_dimen = 170
        '''picture = customtkinter.CTkFrame(contact_window, height=picture_width, width=picture_width, corner_radius=picture_width/2, fg_color=self.color)
        text_pic = customtkinter.CTkLabel(contact_window, text=self.first_name[0].upper(), fg_color=self.color, text_color=PageIcon1.color["white"],
                                          font=customtkinter.CTkFont(family="Inter", size=70, weight="bold"))
        picture.grid(row=1, column=0, pady=default_margin)
        text_pic.grid(row=1, column=0, pady=default_margin)'''

        contact_picture = customtkinter.CTkImage(light_image=PIL.Image.open("images/user.png"),
                                                 dark_image=PIL.Image.open('images/user.png'),
                                                 size=(picture_dimen, picture_dimen))
        contact_pic = customtkinter.CTkButton(contact_window, image=contact_picture, text='',
                                              fg_color=tools_bar_bg_color)
        contact_pic.grid(row=1, column=0, pady=default_margin)

        contact_name = customtkinter.CTkLabel(contact_window, text=self.first_name + self.last_name,
                                              text_color='#FFFFFF',
                                              font=customtkinter.CTkFont(family="Inter", size=20, weight="bold"))
        contact_name.grid(row=2, column=0)

        list_of_numbers = list()
        list_of_numbers.append(self.number_1)
        if self.number_2 != '':
            list_of_numbers.append(self.number_2)

        numbers_container = customtkinter.CTkFrame(contact_window, corner_radius=0)
        numbers_container.columnconfigure(0, weight=1)

        for i, item in enumerate(list_of_numbers):
            numbers_container.rowconfigure(i, weight=0)
            number_box = customtkinter.CTkFrame(numbers_container, corner_radius=0, fg_color=tools_bar_bg_color)
            number_box.columnconfigure(0, weight=0)
            number_box.columnconfigure(1, weight=1)
            number_box.columnconfigure(2, weight=0)

            phone_icon = customtkinter.CTkImage(light_image=PIL.Image.open('images/phone2.png'),
                                                dark_image=PIL.Image.open('images/phone2.png'),
                                                size=(20, 20))
            phone_btn = customtkinter.CTkButton(number_box, width=20, height=20, image=phone_icon,
                                                fg_color=self.color, text='')
            phone_btn.grid(row=i, column=0, sticky='w', padx=default_margin)

            number = customtkinter.CTkLabel(number_box, text=item, text_color='#FFFFFF',
                                            font=customtkinter.CTkFont(family="Inter", size=16))
            number.grid(row=i, column=1, sticky='w')

            sms_icon = customtkinter.CTkImage(light_image=PIL.Image.open('images/sms2.png'),
                                              dark_image=PIL.Image.open('images/sms2.png'),
                                              size=(20, 20))
            sms_btn = customtkinter.CTkButton(number_box, width=30, height=30, image=sms_icon,
                                              fg_color=self.color, text='')
            sms_btn.grid(row=i, column=2, sticky='e', padx=(0, default_margin))

            number_box.grid(row=i, column=0, sticky='nesw')

        numbers_container.grid(row=3, column=0, sticky='nesw', pady=(2 * default_margin, 0))

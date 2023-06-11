import time

# import folium
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
# from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
import qrcode
import threading
import json
# import sqlite3
# from random import randrange

# import discord
# from discord.ext import tasks

import src.vocal_command


# import src.contact as contactclass
# import src.message as messageclass


def back_ground():
    src.vocal_command.read_vocal_data()


bg_task = threading.Thread(target=back_ground, daemon=True)


class StartPage(MDScreen):
    pass


class ConnexionPage(MDScreen):
    text_instructions = [
        "Pour connecter votre téléphone à votre console multimedia, suivez les étapes suivantes ci dessous:",
        "1.  Ouvrez l'application LIION ASSIST sur votre smartphone; Bien vouloir la télécharger sur le Playstore si elle n'est pas encore installée ;",
        "2.  Autorisez l'accès à l'appareil photo, au WIFI, et au micro puis, cliquer sur le bouton CONNECTER pour établir la connection ;",
        "3.  Positionnez votre téléphone face à la console pour scanner le code QR ci dessus;",
        "4.  Une fois connecté, vous pouvez à présent jouir des fonctionnalités offertes par LIION ASSIST."
    ]
    text_instruction = """1.  Ouvrez l'application LIION ASSIST sur votre smartphone; Bien vouloir la télécharger sur le Playstore si elle n'est pas encore installée ;\n2.  Autorisez l'accès à l'appareil photo, au WIFI, et au micro puis, cliquer sur le bouton CONNECTER pour établir la connection ;\n3.  Positionnez votre téléphone face à la console pour scanner le code QR ci dessus;\n4.  Une fois connecté, vous pouvez à présent jouir des fonctionnalités offertes par LIION ASSIST."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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


class HomePage(MDScreen):
    pass


class PhonePage(MDScreen):
    pass


class GpsPage(MDScreen):
    pass


class MusicPage(MDScreen):
    pass


class VideoPage(MDScreen):
    pass


class SettingsPage(MDScreen):
    pass


class MessagePage(MDScreen):
    pass


def load_contact_card(contact, color, *args):
    kivi_code = '''
MDCard:
    on_press: app.load_contact_info("''' + contact + '''") 
    size_hint: 0.9, None
    height: 60
    pos_hint: {'center_x': 0.5}
    md_bg_color: 1, 1, 1, 0
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'horizontal'
            md_bg_color: get_color_from_hex("#C7C7C7")
            radius: 15
            MDBoxLayout:
                size_hint_x: None
                width: 10
            MDAnchorLayout:
                size_hint: None, None
                size: 40, 40
                radius: 20
                pos_hint: {'center_y': 0.5}
                md_bg_color: "''' + color + '''"
                MDLabel:
                    text: "''' + contact[0].upper() + '''"
                    font_size: 20
                    color: get_color_from_hex("#FFFFFF")
                    valign: 'middle'
                    halign: 'center'
            MDBoxLayout:
                size_hint_x: None
                width: 20
            MDBoxLayout:
                orientation: 'vertical'
                MDBoxLayout:
                    size_hint_y: 1.7
                    MDLabel:
                        text: "''' + contact.capitalize() + '''"
                        anchor: 'left'
                        font_size: 17
        MDBoxLayout:
            size_hint_y: None
            height: 10

    '''
    return kivi_code


def time_sms(m):
    return m[1]


class App(MDApp):
    default_text_color = "#C9C5C5"
    default_bg_color = "#0F0332"
    default_bar_color = "#39585B"
    con = ''
    c = src.vocal_command.donnees_vocales
    sm = ScreenManager(transition=SlideTransition())
    with open("data_base/data.json") as json_file:
        messages = json.load(json_file)

    def build(self):
        Window.size = [836, 584]
        self.title = "LIION ASSIST"
        self.load_all_kv_files()
        screens = [
            StartPage(name='LIION'),
            ConnexionPage(name='CONNECTION'),
            HomePage(name='home'),
            PhonePage(name='phone'),
            MessagePage(name='message'),
            GpsPage(name='gps'),
            MusicPage(name='music'),
            VideoPage(name='video'),
            SettingsPage(name='settings')
        ]

        for screen in screens:
            self.sm.add_widget(screen)
        self.load_chatlist()
        self.load_contacts()
        bg_task.start()

        return self.sm

    def on_start(self):
        src.vocal_command.text_to_voicenote("Bienvenue sur Liion Assist !")
        self.toscreen1()
        Clock.schedule_interval(self.check_instruction, 0.01)

    def order_message(self, contact, *args):
        order = []
        a = 0
        for key in ["sent", "received"]:
            for i in range(len(contact[key])):
                order.append(contact[key][i])
                order[a].append(key)
                a += 1
        return sorted(order, key=time_sms)

    def load_discussion(self, contact, *args):
        w = Builder.load_file('kivy/chat_container.kv')
        self.sm.screens[4].ids.chat.clear_widgets()
        self.sm.screens[4].ids.chat.add_widget(w)
        text = self.order_message(self.messages[contact])
        e = Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDLabel:
    text: '   """ + contact.capitalize() + """'
    font_size: 20
    color: get_color_from_hex("#FFFFFF")
    pos_hint: {"x": 0.5, "center_y": 0.5}"""
                                )
        w.ids.entete.add_widget(e)
        for i in range(len(text)):
            if len(text[i][0]) <= 30:
                taille = 10 * len(text[i][0]) + 10
            else:
                taille = 300
            hauteur = 10 + 18 * (1 + int(len(text[i][0])) / 30)
            t1 = MDLabel(text="" + text[i][0] + "  ", font_size=14)

            if text[i][2] == 'sent':
                pos = """ "right": 1 """
            else:
                pos = """ "x": 0 """
            ar = Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: get_color_from_hex("#C7C7C7")
    size_hint: None, None
    size: """ + str(taille) + """, """ + str(hauteur) + """
    radius: 10
    padding: 7, 0, 7, 0
    pos_hint: {""" + pos + """, "top": 1}""")
            ar.add_widget(t1)
            a = MDFloatLayout(size_hint={1, None}, size={0, hauteur + 10}, pos_hint={"center_x": 0.5, "top": 1})
            a.add_widget(ar)
            w.ids.messages.add_widget(a)

    def change_screen(self, screen):
        self.sm.current = screen

    def toscreen1(self, *args):
        self.sm.current = 'LIION'
        Clock.schedule_once(lambda x: self.change_screen("CONNECTION"), 10)

    def load_chatlist(self):
        # self.send_new_sms("jdkf", 202305251639, "mambou")
        # self.receive_new_sms("ça veut dire quoi?", 202305251645, "mambou")
        # self.receive_new_sms("yo", 202305251645, "jean")
        for contact in self.messages.keys():
            card = Builder.load_string("""
MDCard:
    on_press: app.load_discussion('""" + contact + """')
    size_hint: 0.9, None
    height: 60
    pos_hint: {'center_x': 0.5}
    md_bg_color: 1, 1, 1, 0""")
            w = Builder.load_file('kivy/discussion_card.kv')
            self.sm.screens[4].ids.chatlist.add_widget(card)
            card.add_widget(w)
            text = self.order_message(self.messages[contact])
            if not text:
                date = ''
                last_sms = ''
            else:
                date = str(text[-1][1])[:4] + '/' + str(text[-1][1])[4:6] + '/' + str(text[-1][1])[6:8] + '  ' + str(
                    text[-1][1])[8:10] + 'h' + str(text[-1][1])[10:]
                last_sms = text[-1][0]
            a = Builder.load_string("""
MDLabel:
    id: contact
    text: '""" + contact.capitalize() + """'
    anchor: 'left'
    font_size: 18"""
                                    )
            b = Builder.load_string("""
MDLabel:
    text: '""" + date + """'
    anchor: 'right'
    font_size: 10"""
                                    )
            c = Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDLabel:
    text: '""" + last_sms + """'
    anchor: 'left'
    font_size: 12
    color: get_color_from_hex("#4E4C4C")"""
                                    )
            d = Builder.load_string("""
MDBoxLayout:
    md_bg_color: '""" + self.messages[contact]["color"] + """'
    radius: 20
    size: self.minimum_width, self.minimum_height
    MDLabel:
        text: '""" + contact[0].upper() + """'
        anchor: 'right'
        font_size: 22
        color: 'white'
        valign: 'middle'
        halign: 'center'"""
                                    )
            w.ids.discus_inf.add_widget(a)
            w.ids.discus_inf.add_widget(b)
            w.ids.last_sms.add_widget(c)
            w.ids.initial.add_widget(d)

    def load_contacts(self):
        i = 0
        for contact in self.messages:
            kv = Builder.load_string(load_contact_card(contact, self.messages[contact]["color"]))
            self.sm.screens[3].ids.contact_list.add_widget(kv)
            i += 1

    def load_contact_info(self, contact, *args):
        w = Builder.load_file('kivy/contact_info.kv')
        self.sm.screens[3].ids.right_content.clear_widgets()
        self.sm.screens[3].ids.right_content.add_widget(w)
        a1 = Builder.load_string("""
MDIconButton:
    icon: 'images/phone2.png'
    icon_size: '30sp'""")
        a2 = Builder.load_string("""
MDLabel:
    text: '  """ + str(self.messages[contact]["number"]) + """'
    font_size: 20
    color: 'white'""")
        a3 = Builder.load_string("""
MDIconButton:
    icon: 'images/sms2.png'
    icon_size: '30sp'
    halign: 'right' """)
        b1 = Builder.load_string("""
Image:
    size_hint: None, None
    size: 180, 180
    source: 'images/user.png'
    pos_hint: {'center_x': 0.5, 'top': 1}""")
        b2 = Builder.load_string("""
MDLabel:
    text: '""" + contact.capitalize() + """'
    font_size: 30
    halign: "center"
    color: 'white'""")
        w.ids.number.add_widget(a1)
        w.ids.number.add_widget(a2)
        w.ids.number.add_widget(a3)
        w.ids.name.add_widget(b1)
        w.ids.name.add_widget(b2)

    def add_contact(self, nom, number, color, *args):
        mess = self.messages
        mess.update({nom: {'number': number, 'color': color, 'sent': [], 'received': []}})
        with open("data_base/data.json", 'w') as json_file:
            json.dump(mess, json_file, indent=4)

    def send_new_sms(self, sms, date, contact, number, color, *args):
        mess = self.messages
        if contact not in mess.keys():
            self.add_contact(contact, number, color)
        mess[contact]['sent'].append([sms, date])
        with open("data_base/data.json", 'w') as json_file:
            json.dump(mess, json_file, indent=4)

    def receive_new_sms(self, sms, date, contact, number, color, *args):
        mess = self.messages
        if contact not in mess.keys():
            self.add_contact(contact, number, color)
        mess[contact]['received'].append([sms, date])
        with open("data_base/data.json", 'w') as json_file:
            json.dump(mess, json_file, indent=4)

    def load_all_kv_files(self, **kwargs):
        Builder.load_file('kivy/start_page.kv')
        Builder.load_file('kivy/connexion_page.kv')
        Builder.load_file('kivy/home_page.kv')
        Builder.load_file('kivy/phone_page.kv')
        Builder.load_file('kivy/gps_page.kv')
        Builder.load_file('kivy/music_page.kv')
        Builder.load_file('kivy/video_page.kv')
        Builder.load_file('kivy/settings_page.kv')
        Builder.load_file('kivy/message_page.kv')

    def check_instruction(self, *args):
        if src.vocal_command.donnees_vocales[-1] == "accueil":
            self.change_screen('home')
        if src.vocal_command.donnees_vocales[-1] == "message":
            self.change_screen('message')
        if "affiche discussion" in src.vocal_command.donnees_vocales[-1]:
            if src.vocal_command.donnees_vocales[-1] == "affiche discussion":
                src.vocal_command.text_to_voicenote("repetez")
                time.sleep(1)
            else:
                self.load_discussion(src.vocal_command.donnees_vocales[-1].split(" ")[2])
        if src.vocal_command.donnees_vocales[-1] == "fin":
            self.stop()


app = App()

if __name__ == "__main__":
    app.run()
    src.vocal_command.text_to_voicenote("Au revoir, à la prochaine !")

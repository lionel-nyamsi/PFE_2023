from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
import qrcode
import threading
import json

# import discord
# from discord.ext import tasks

import src.vocal_command


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


def time_sms(m):
    return m[1]


class App(MDApp):
    default_text_color = "#C9C5C5"
    default_bg_color = "#0F0332"
    default_bar_color = "#39585B"
    c = src.vocal_command.donnees_vocales
    sm = ScreenManager(transition=SlideTransition())
    with open("donnee_test.json") as json_file:
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
        bg_task.start()
        self.order_message(self.messages['papa'])

        return self.sm

    def on_start(self):
        src.vocal_command.text_to_voicenote("Bienvenue sur Liion Assist !")
        self.toscreen1()
        Clock.schedule_interval(self.check_instruction, 0.01)

    def order_message(self, contact, *args):
        order = []
        a = 0
        for key in contact:
            for i in range(len(contact[key])):
                order.append(contact[key][i])
                order[a].append(key)
                a += 1
        return sorted(order, key=time_sms)

    def load_discussion(self):
        w = Builder.load_file('kivy/chat_container.kv')
        self.sm.screens[4].ids.chat.clear_widgets()
        self.sm.screens[4].ids.chat.add_widget(w)
        text = self.order_message(self.messages['papa'])
        for i in range(len(text)):
            if len(text[i][0]) <= 500:
                taille = 10*len(text[i][0])+10
            else:
                taille = 500
            t1 = MDLabel(text="  "+text[i][0]+"  ", font_size=14)

            if text[i][2] == 'sent':
                pos = """ "x": 0 """
            else:
                pos = """ "right": 1 """
            ar = Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: get_color_from_hex("#C7C7C7")
    size_hint: None, None
    size: """ + str(taille) + """, 40
    radius: 10
    pos_hint: {""" + pos + """, "top": 1}""")
            ar.add_widget(t1)
            a = MDFloatLayout(size_hint={1, None}, size={0, 50}, pos_hint={"center_x": 0.5, "top": 1})
            a.add_widget(ar)
            w.ids.messages.add_widget(a)

    def change_screen(self, screen):
        self.sm.current = screen

    def toscreen1(self, *args):
        self.sm.current = 'LIION'
        Clock.schedule_once(lambda x: self.change_screen("CONNECTION"), 10)

    def load_chatlist(self):
        for contact in self.messages:
            w = Builder.load_file('kivy/discussion_card.kv')
            self.sm.screens[4].ids.chatlist.add_widget(w)

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
        if src.vocal_command.donnees_vocales[-1] == "affiche discussion":
            self.load_discussion()
        if src.vocal_command.donnees_vocales[-1] == "fin":
            self.stop()


app = App()

if __name__ == "__main__":

    app.run()
    src.vocal_command.text_to_voicenote("Au revoir, à la prochaine !")

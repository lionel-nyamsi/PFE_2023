from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder

import qrcode
import threading
import json
import sqlite3
from random import randrange

import discord
from discord.ext import tasks

import src.vocal_command
import src.contact as contactClass
import src.message as messageClass


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


def load_contact_card(contact):
    contact_name = contact.name
    contact_color = contact.color
    contact_letter = contact_name[0]

    KIVY_CODE = '''
MDCard:
    on_press: ''' + str(contact.display_contact_info()) + '''
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
                md_bg_color: "''' + contact_color + '''"
                MDLabel:
                    text: "''' + contact_letter + '''"
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
                        text: "''' + contact_name + '''"
                        anchor: 'left'
                        font_size: 17
        MDBoxLayout:
            size_hint_y: None
            height: 10

    '''
    return KIVY_CODE


class App(MDApp):
    default_text_color = "#C9C5C5"
    default_bg_color = "#0F0332"
    default_bar_color = "#39585B"
    c = src.vocal_command.donnees_vocales
    sm = ScreenManager(transition=SlideTransition())
    with open("donnee_sms.json") as json_file:
        messages = json.load(json_file)

    contact_list = []
    messages_list = []

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
        Clock.schedule_once(self.toscreen1, 3)
        Clock.schedule_interval(self.check_instruction, 0.01)

    def load_discussion(self):
        w = Builder.load_file('kivy/chat_container.kv')
        self.sm.screens[4].ids.chat.clear_widgets()
        self.sm.screens[4].ids.chat.add_widget(w)
        for i in range(max(len(self.messages['sent']), len(self.messages['received']))):
            t1 = MDLabel(text=self.messages['sent'][i], font_size="14")
            ar = MDBoxLayout(md_bg_color="#C7C7C7", size_hint={0.5, None}, size={0, 40}, radius=10, pos_hint={"x": 0, "top": 1})
            ar.add_widget(t1)
            t2 = MDLabel(text=self.messages['received'][i], font_size="14", halign='right')
            br = MDBoxLayout(md_bg_color="#C7C7C7", size_hint={0.5, None}, size={0, 40}, radius=10, pos_hint={"right": 1, "top": 1})
            br.add_widget(t2)
            a = MDCard(size_hint={1, None}, size={0, 50}, pos_hint={"center_x": 0.5, "top": 1})
            b = MDCard(size_hint={1, None}, size={0, 50}, pos_hint={"center_x": 0.5, "top": 1})
            a.add_widget(ar)
            b.add_widget(br)

            w.ids.messages.add_widget(a)
            w.ids.messages.add_widget(b)

    def change_screen(self, screen):
        self.sm.current = screen

    def toscreen1(self, *args):
        self.sm.current = 'CONNECTION'

    def load_chatlist(self):
        '''
        try:
            connection = sqlite3.connect("data_base/db_liionAssist.db")
            cursor = connection.cursor()

            # request 1 -> for sent messages
            request = 'SELECT name_reciever, phonenumber, message_content, date_sending, time_sending FROM sent_message'
            result = cursor.execute(request)

            for sms in result.fetchall():
                print(sms)
                message = messageClass.Message("user", sms[0], sms[1], sms[2], sms[3], sms[4])
                self.messages_list.append(message)

            # request 2 -> for recieved messages
            request = 'SELECT name_sender, phonenumber, message_content, date_reception, time_reception FROM recieved_message'
            result = cursor.execute(request)

            for sms in result.fetchall():
                print(sms)
                message = messageClass.Message(sms[0], "user", sms[1], sms[2], sms[3], sms[4])
                self.messages_list.append(message)

        except Exception as error:
            print("[ERROR] : {}".format(error))
            connection.rollback()

        finally:
            connection.close()  '''

        w = []
        for i in range(5):
            w.append(Builder.load_file('kivy/discussion_card.kv'))
            self.sm.screens[4].ids.chatlist.add_widget(w[i])

    def load_contacts(self):

        colors = ["green", "red", "yellow", "pink", "violet", "blue", "orange"]

        try:
            connection = sqlite3.connect("data_base/db_liionAssist.db")
            cursor = connection.cursor()

            request = 'SELECT name, firstname, phonenumber1, phonenumber2, phonenumber3 FROM contact'
            result = cursor.execute(request)

            for contact in result.fetchall():
                print(contact)
                if contact[1] is not None and contact[1] != "":
                    name = contact[0] + " " + contact[1]
                else:
                    name = contact[0]
                phonenumber1 = contact[2]
                if contact[3] is not None or contact[3] != "":
                    phonenumber2 = contact[3]
                else:
                    phonenumber2 = ""
                if contact[4] is not None or contact[4] != "":
                    phonenumber3 = contact[4]
                else:
                    phonenumber3 = ""

                color = colors[randrange(len(colors))]
                contact_ = contactClass.Contact(name, phonenumber1, color, phonenumber2, phonenumber3)
                self.contact_list.append(contact_)

            w = []
            for i in range(len(self.contact_list)):
                KV = load_contact_card(self.contact_list[i])
                w.append(Builder.load_string(KV))
                self.sm.screens[3].ids.contact_list.add_widget(w[i])

        except Exception as error:
            print("[ERROR] : {}".format(error))
            connection.rollback()

        finally:
            connection.close()

    def load_contact_info(self):
        for contact in self.contact_list:
            print(contact)

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
        if src.vocal_command.donnees_vocales[-1] == "téléphone":
            self.change_screen('phone')
        if src.vocal_command.donnees_vocales[-1] == "affiche discussion":
            self.load_discussion()
        if src.vocal_command.donnees_vocales[-1] == "fin":
            self.stop()


app = App()

if __name__ == "__main__":

    app.run()
    src.vocal_command.text_to_voicenote("Au revoir, à la prochaine !")

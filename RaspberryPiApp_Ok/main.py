from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
import qrcode


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


class App(MDApp):
    default_text_color = "#C9C5C5"
    default_bg_color = "#0F0332"
    default_bar_color = "#39585B"

    def build(self):
        Window.size = [836, 584]
        self.title = "LIION ASSIST"
        self.load_all_kv_files()
        self.sm = ScreenManager(transition=SlideTransition())

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

        return self.sm

    def on_start(self):
        Clock.schedule_once(self.toscreen1, 3)

    def load_discussion(self):
        w = Builder.load_file('kivy/chat_container.kv')
        self.sm.screens[4].ids.chat.clear_widgets()
        self.sm.screens[4].ids.chat.add_widget(w)

    def change_screen(self, screen):
        self.sm.current = screen

    def toscreen1(self, *args):
        self.sm.current = 'CONNECTION'

    def load_chatlist(self):
        w = []
        for i in range(50):
            w.append(Builder.load_file('kivy/discussion_card.kv'))
            self.sm.screens[4].ids.chatlist.add_widget(w[i])

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


if __name__ == "__main__":
    App().run()

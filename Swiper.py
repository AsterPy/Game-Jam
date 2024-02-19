import sqlite3
import time
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
import random

class Main(MDScreen):
    click_sound = None
    button_clicked = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not Main.click_sound:
            Main.click_sound = SoundLoader.load('click.mp3')


class CustomButton(Button):
    pass

class CustomBlock1(Button):
    pass

class CustomBlock2(Button):
    pass

class CustomBlock3(Button):
    pass

class WelcomeScreen(Screen):
    player = None  # Зробимо player статичним атрибутом класу
    sound = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        if WelcomeScreen.player is None:  # Перевіряємо, чи player вже був створений
            WelcomeScreen.player = VideoPlayer(source='video.mp4', state='play', options={'allow_stretch': True})
            WelcomeScreen.player.state = 'play'
            WelcomeScreen.player.size_hint = (1, 1)
            WelcomeScreen.player.pos_hint = {'x': 0, 'y': 0}
            WelcomeScreen.player.options = {'eos': 'loop'}
            WelcomeScreen.player.allow_stretch = True
            WelcomeScreen.player.volume = 0.2
        button = CustomButton()
        block1 = CustomBlock1()
        block2 = CustomBlock2()
        block3 = CustomBlock3()
        button.bind(on_release=self.on_button_click)
        layout.add_widget(WelcomeScreen.player)
        layout.add_widget(block1)
        layout.add_widget(block2)
        layout.add_widget(block3)
        layout.add_widget(button)
        self.add_widget(layout)

    def on_button_click(self, instance):
        self.manager.current = 'main'

        WelcomeScreen.player.state = 'stop'
        if not WelcomeScreen.sound:
            WelcomeScreen.sound = SoundLoader.load('BG.mp3')  
            if WelcomeScreen.sound:
                WelcomeScreen.sound.loop = True 
                WelcomeScreen.sound.volume = 0.2
                WelcomeScreen.sound.play()


class ProgramApp(MDApp):
    title = "App"
    Window.size = (380, 800)
    db_name = "click.db"
    button_state = 0

    def build(self):
        self.theme_cls.theme_style = "Dark"  
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome_screen'))  # Додаємо екран вітання перед Main
        sm.add_widget(Main(name='main'))
        return sm
    
    def change_dragon_image(self):
        dragon_images = ['img/dragon_img-1.png', 'img/dragon_img-2.png', 'img/dragon_img-3.png', 'img/dragon_img-4.png', 'img/dragon_img-5.png', 'img/dragon_img-6.png', 'img/dragon_img-7.png', 'img/dragon_img-8.png', 'img/dragon_img-9.png', 'img/dragon_img-10.png']
        random_image = random.choice(dragon_images)
        self.root.get_screen('main').ids.background.source = random_image

    def on_click(self):
        coins_label = self.root.get_screen('main').ids.coins
        coins = int(coins_label.text)

        if 1 < coins < 5:
            self.root.get_screen('main').ids.background.source = 'img/screen-1.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 5 < coins < 30:
            self.root.get_screen('main').ids.background.source = 'img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 30 < coins < 35:
            self.root.get_screen('main').ids.background.source = 'img/screen-2.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 35 < coins < 40:
            self.root.get_screen('main').ids.background.source = 'img/screen-3.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 40 < coins < 85:
            self.root.get_screen('main').ids.background.source = 'img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 85 < coins < 95:
            self.root.get_screen('main').ids.background.source = 'img/screen-4.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 95 < coins < 250:
            self.root.get_screen('main').ids.background.source = 'img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 250 < coins < 260:
            self.root.get_screen('main').ids.background.source = 'img/screen-5.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 260 < coins < 265:
            self.root.get_screen('main').ids.background.source = 'img/screen-6.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 265 < coins < 340:
            self.root.get_screen('main').ids.background.source = 'img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 340 < coins < 350:
            self.root.get_screen('main').ids.background.source = 'img/screen-7.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 350 < coins < 355:
            self.root.get_screen('main').ids.background.source = 'img/screen-8.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 355 < coins < 490:
            self.root.get_screen('main').ids.background.source = 'img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 490 < coins < 500:
            self.root.get_screen('main').ids.background.source = 'img/screen-9.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 500 < coins < 505:
            self.root.get_screen('main').ids.background.source = 'img/screen-10.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 505 < coins < 900:
            self.root.get_screen('main').ids.background.source = 'img/screen.png'
            coins_label.text = str(coins + 5)
            self.save_click_count(coins_label.text)
        if 900 < coins < 910:
            self.root.get_screen('main').ids.background.source = 'img/screen-11.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 910 < coins < 930:
            self.root.get_screen('main').ids.background.source = 'img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 930 < coins < 940:
            self.root.get_screen('main').ids.background.source = 'img/screen-12.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 940 < coins < 945:
            self.root.get_screen('main').ids.background.source = 'img/screen-13.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 945 < coins < 960:
            self.root.get_screen('main').ids.background.source = 'img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 960 < coins < 970:
            self.root.get_screen('main').ids.background.source = 'img/screen-14.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 970 < coins < 975:
            self.root.get_screen('main').ids.background.source = 'img/screen-15.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 975 < coins < 1090:
            self.root.get_screen('main').ids.background.source = 'img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1090 < coins < 1100:
            self.root.get_screen('main').ids.background.source = 'img/screen-16.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1100 < coins < 1105:
            self.root.get_screen('main').ids.background.source = 'img/screen-17.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1105 < coins < 1110:
            self.root.get_screen('main').ids.background.source = 'img/screen-18.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1110 < coins < 1115:
            self.root.get_screen('main').ids.background.source = 'img/screen-19.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1115 < coins < 1125:
            self.root.get_screen('main').ids.background.source = 'img/screen-20.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1125 < coins < 1130:
            self.root.get_screen('main').ids.background.source = 'img/screen-21.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1130 < coins < 1280:
            self.root.get_screen('main').ids.background.source = 'img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1280 < coins < 1290:
            self.root.get_screen('main').ids.background.source = 'img/screen-22.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1290 < coins < 1300:
            self.root.get_screen('main').ids.background.source = 'img/screen-23.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1300 < coins < 1305:
            self.root.get_screen('main').ids.background.source = 'img/screen-24.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1305 < coins < 1400:
            self.root.get_screen('main').ids.background.source = 'img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1400 < coins < 1410:
            self.root.get_screen('main').ids.background.source = 'img/screen-25.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1410 < coins < 1415:
            self.root.get_screen('main').ids.background.source = 'img/screen-26.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1415 < coins < 1490:
            self.root.get_screen('main').ids.background.source = 'img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1490 < coins < 1500:
            self.root.get_screen('main').ids.background.source = 'img/screen-27.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1500 < coins < 1510:
            self.root.get_screen('main').ids.background.source = 'img/screen-28.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1510 < coins < 1590:
            self.root.get_screen('main').ids.background.source = 'img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1590 < coins < 1600:
            self.root.get_screen('main').ids.background.source = 'img/screen-29.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1600 < coins < 1610:
            self.root.get_screen('main').ids.background.source = 'img/screen-30.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1610 < coins < 1620:
            self.root.get_screen('main').ids.background.source = 'img/screen-31.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        else:
            if 505 < coins < 900:
                self.root.get_screen('main').ids.background.source = 'img/screen.png'
                coins_label.text = str(coins + 5)
                self.save_click_count(coins_label.text)
            else:
                coins_label.text = str(coins + 1)
                self.save_click_count(coins_label.text)

        if self.button_state == 0:
            anim = Animation(size_hint=(0.25, 1),pos_hint={'center_x': 0.5, 'center_y': 0.5}, duration=0.1)
            self.button_state = 1
        else:
            anim = Animation(size_hint=(0.2, 1), duration=0.1)
            self.button_state = 0

        anim.start(coins_label)

        if Main.button_clicked == True:
            Main.click_sound.volume = 0.2
            Main.click_sound.play()
        if Main.button_clicked == False:
            Main.button_clicked = True
        

    def save_click_count(self, count):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM clicks")
        c.execute("INSERT INTO clicks VALUES (?)", (count,))
        conn.commit()
        conn.close()

    def load_click_count(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM clicks")
        result = c.fetchone()
        conn.close()
        return str(result[0]) if result else "0"
    
    def on_start(self):
        coins_label = self.root.get_screen('main').ids.coins
        coins_label.text = self.load_click_count()
    
if __name__ == '__main__':
    LabelBase.register(name="Press Start 2P",
                    fn_regular='./font/PressStart2P-Regular.ttf')
    app = ProgramApp()
    app.run()

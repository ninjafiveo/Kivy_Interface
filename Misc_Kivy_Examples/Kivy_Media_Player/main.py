import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer
from numpy import source

class MainApp(MDApp):
    title = "Simple Video"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create instance of video player
        player = VideoPlayer(source = 'Side Projects/Kivy_Interface/Misc_Kivy_Examples/Kivy_Media_Player/mp.mp4')
        # Assign video player state
        player.state = 'play'
        player.options = {'eos': 'loop'} #? loop stop

        #Allow Stretch
        player.allow_stretch = True

        # Return Player
        return player
MainApp().run()


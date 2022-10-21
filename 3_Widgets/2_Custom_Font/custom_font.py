from ast import Global
from glob import glob
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from numpy import size
from kivy.metrics import dp # needed to density pixels size.
from kivy.uix.scrollview import ScrollView
from pygame import CONTROLLER_AXIS_LEFTX
from kivy.properties import StringProperty #! Import to customize properties in the kivy document.

# the_count = 0 #normally would declare vars here and make them global, but in this case we are going to use the self keyword.

# Video Ends at 1:18:00

class WidgetsExample(GridLayout):
    the_count = 0
    my_text = StringProperty(str(the_count)) #!have to create a custom property

    def on_button_click(self):
        # global the_count
        # self.the_count += 1
        print("Ninja Ninja")
        self.my_text = str(self.the_count)
        if self.the_count >= 10:
            self.my_text = "Game Over"
        else:
            self.the_count += 1
            print("Ninja Ninja")
            self.my_text = str(self.the_count)

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super(). __init__(**kwargs)
        # self.orientation ="lr-bt"     # Orientation from left-right("rl-tb", "rl-bt", "lr-tb", "lr-bt") and top-bottom
        for i in range(0, 1000):
            # size = dp(100) + i*10
            size = dp(100) 
            # b = Button(text = str(i+1), size_hint=(.1, .1))
            # b = Button(text = str(i+1), size_hint=(None, None), size = (150, 150))
            # b = Button(text = str(i+1), size_hint=(None, None), size = (dp(150), dp(150)))
            b = Button(text = str(i+1), size_hint=(None, None), size = (dp(size), dp(size)))
            self.add_widget(b)



# class GridLayoutExample(GridLayout):
#     pass
#! ^^^ Isn't actually needed. Can be defined in the .kv file with @GridLayout

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class ButtonApp(App):
    pass

ButtonApp().run()

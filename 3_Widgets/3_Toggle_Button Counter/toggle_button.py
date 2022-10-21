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
import time

# the_count = 0 #normally would declare vars here and make them global, but in this case we are going to use the self keyword.

# Video Ends at 1:18:00

class WidgetsExample(GridLayout):
    the_count = 0
    the_timer = 0
    my_text = StringProperty(str(the_count)) #!have to create a custom property
    my_timer = StringProperty(str(the_timer))

    def on_button_click(self):
        self.my_text = str(self.the_count)
        if self.the_count >= 10:
            self.my_text = "Game\nOver"
        else:
            self.the_count += 1
            print("Ninja Ninja")
            self.my_text = str(self.the_count)
    
    def on_toggle_button_state(self, widget): #the self here is for the object/class the "widget" is to pass back and forth to the kv document.
        print(f"Toggle State: {widget.state}")
        self.my_timer = str(self.the_timer)
        if widget.state == "normal":
            # OFF
            widget.text = "OFF" 
        else:
            # ON
            widget.text = "ON"
            self.the_timer += 1
            self.my_timer = str(self.the_timer)
            while True:
                time.sleep(5)
                print("Bob")
            #     pass
                # time.sleep(1)
            #     self.the_timer += 1
            #     self.my_timer = str(self.the_timer)
                

            

        

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

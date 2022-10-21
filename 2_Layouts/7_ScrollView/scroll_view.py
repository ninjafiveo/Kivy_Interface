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

class Scroll_ViewApp(App):
    pass

Scroll_ViewApp().run()

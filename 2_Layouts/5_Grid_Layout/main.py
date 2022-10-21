from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.gridlayout import GridLayout

# class GridLayoutExample(GridLayout):
#     pass
#! ^^^ Isn't actually needed. Can be defined in the .kv file with @GridLayout

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class Grid_LayoutApp(App):
    pass

Grid_LayoutApp().run()

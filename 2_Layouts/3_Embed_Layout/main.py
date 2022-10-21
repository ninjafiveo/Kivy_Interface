from kivy.app import App        #App Class - Allows you to run Kivy
from kivy.uix.boxlayout import BoxLayout        # For BoxLayout
from kivy.uix.widget import Widget      #This is the main interface of the object (App)
from kivy.uix.button import Button #This is so we can put the button in the code below. 

class BoxLayoutExample(BoxLayout): #need to change out kv file from mainwidget to boxlayoutexample.
    #! Usually you only use the kv file, but here is an example with the code. There are use cases for it to be in the code.
    pass

class MainWidget(Widget):       #This is the main interface of the object (App)
    pass

class Embed_LayoutApp(App):           #App Class - Allows you to run Kivy
    pass

Embed_LayoutApp().run()

#! This is the base set up for every Kivy app. 
#! You have to substanciate the Kivy object at the end with the class "Embed_LayoutApp()" and select the run() method.
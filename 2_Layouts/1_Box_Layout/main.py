from kivy.app import App        #App Class - Allows you to run Kivy
from kivy.uix.boxlayout import BoxLayout        # For BoxLayout
from kivy.uix.widget import Widget      #This is the main interface of the object (App)
from kivy.uix.button import Button #This is so we can put the button in the code below. 

class BoxLayoutExample(BoxLayout): #need to change out kv file from mainwidget to boxlayoutexample.
    #! Usually you only use the kv file, but here is an example with the code. There are use cases for it to be in the code.
    pass
"""
    def __init__(self, **kwargs): # **kwargs is for the inner workings of kivy.
        super().__init__(**kwargs)
        self.orientation = 'vertical' #changes the boxlayout from horizontal(default) to vertical.
        b1 = Button(text = "A")
        b2 = Button(text = "B")
        b3 = Button(text = "C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        # ^^^ This is how it works in code. Moving it to the .kv file next. 
"""

class MainWidget(Widget):       #This is the main interface of the object (App)
    pass

class TheBoxLayoutApp(App):           #App Class - Allows you to run Kivy
    pass

TheBoxLayoutApp().run()

#! This is the base set up for every Kivy app. 
#! You have to substanciate the Kivy object at the end with the class "TheBoxLayoutApp()" and select the run() method.
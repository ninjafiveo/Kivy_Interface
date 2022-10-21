
from kivy.app import App        #App Class - Allows you to run Kivy
from kivy.uix.widget import Widget      #This is the main interface of the object (App)

class MainWidget(Widget):       #This is the main interface of the object (App)
    pass

class TheLabApp(App):           #App Class - Allows you to run Kivy
    pass

TheLabApp().run()

#! This is the base set up for every Kivy app. 
#! You have to substanciate the Kivy object at the end with the class "TheLabApp()" and select the run() method.
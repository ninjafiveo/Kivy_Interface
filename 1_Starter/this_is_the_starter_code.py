from kivy.app import App

class TheLabApp(App):
    pass

TheLabApp().run()

#! This is the base set up for every Kivy app. 
#! You have to substanciate the Kivy object at the end with the class "TheLabApp()" and select the run() method.


#!!!!! Note, if there is .kv file in the same folder it will create an error because the MainWidget File is MIA. But if you move it to another folder, it will run just fine.
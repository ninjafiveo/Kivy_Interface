import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


# You have to have an app class and build method.

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1

        #image widget
        self.window.add_widget(Image(source="logo.png"))

        #Label widget
        self.greeting = Label(
            text = "What's your wallet address? ",
            font_size = 50,
            color = "#00FFCE"
            )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
            multiline = False,
            padding_y = (20, 20),
            size_hint = (1, 0.5),
            font_size = 50

            )
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
            text ="Greet",
            size_hint = (1, 0.5),
            font_size = 35,
            bold = True,
            background_color = "#666666",
            background_normal = ""

            )
        self.window.add_widget(self.button)
        self.button.bind(on_press = self.callback)
        
        #! Time to style
        self.window.size_hint = (0.6, 0.7) # makes the element shrink to 60% of width, 70% of height.
        self.window.pos_hint={"center_x": 0.5, "center_y":0.5}
        

        
        return self.window



    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text+"!"




if __name__ == "__main__":
    SayHello().run()
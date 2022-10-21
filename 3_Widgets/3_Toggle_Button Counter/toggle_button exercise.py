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
import multiprocessing as mp
import math

# #region Multiprocessing Test
# results_a = []
# results_b = []
# results_c = []

# def make_calculation_one(numbers):
#     for number in numbers:
#         results_a.append(math.sqrt(number**3))

# def make_calculation_two(numbers):
#     for number in numbers:
#         results_a.append(math.sqrt(number**4))

# def make_calculation_three(numbers):
#     for number in numbers:
#         results_a.append(math.sqrt(number**5))

# if __name__ == '__main__': #! This statement is required for multiprocessing. 
#     # pass
#     number_list = list(range(5000))
#     p1 = mp.Process(target=make_calculation_one, args=(number_list,))
#     p2 = mp.Process(target=make_calculation_two, args=(number_list,))
#     p3 = mp.Process(target=make_calculation_three, args=(number_list,))
    
#     #! With processes
#     start = time.time() 
#     p1.start()
#     p2.start()
#     p3.start()
#     # make_calculation_one(number_list)
#     # make_calculation_two(number_list)
#     # make_calculation_three(number_list)
#     end = time.time()
#     print(f"WITH Processes: Finished in {end-start} seconds")
#     #! Without processes
#     start = time.time() 
#     make_calculation_one(number_list)
#     make_calculation_two(number_list)
#     make_calculation_three(number_list)
#     end = time.time()
#     print(f"Without Processes: Finished in {end-start} seconds")
# #endregion

class WidgetsExample(GridLayout):
    the_count = 0
    # the_timer = 0 #This is what's going to count up when toggle on
    count_enabled = False #! This is to determine what state the toggle button is in.
    my_text = StringProperty(str(the_count)) #?have to create a custom property
    # my_timer = StringProperty(str(the_timer)) # This takes the value of the_timer and passes it through to the string in the .kv file.

    # def timer_function(self):
    #     self.the_timer
    #     while self.the_timer<30:
    #         self.the_timer+=1
    #         print(self.the_timer)
    # timer_function(the_timer)

    def on_button_click(self):
        self.my_text = str(self.the_count)

        if self.count_enabled: #! Check of count enabled is True. By default is True. But, if self.count_enabled == True: also works.
            if self.the_count >= 10:
                self.my_text = "Game\nOver"
            else:
                self.the_count += 1
                print("Ninja Ninja")
                self.my_text = str(self.the_count)
    

    def on_toggle_button_state(self, widget): #the self here is for the object/class the "widget" is to pass back and forth to the kv document.
        print(f"Toggle State: {widget.state}")
        if widget.state == "normal":
            # OFF
            widget.text = "OFF" 
            self.count_enabled = False
        else:
            # ON
            widget.text = "ON"
            self.count_enabled = True


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

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.vertex_instructions import Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import Clock

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    slider_value_txt = StringProperty("0")
    text_input_str = StringProperty("foo")
    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled:
            self.count = self.count + 1
            self.my_text = str(self.count)
    
    def on_toggle_button_state(self,widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            self.count_enabled = True 
            widget.text = "ON"  
    
    def on_switch_active(self,widget): 
        print("Switch: " + str(widget.active))

    def on_slider_value(self,widget):
        print("Slider: " + str(int(widget.value)))

        self.slider_value_txt = str(int(widget.value))

        print("Slider: " + str(int(widget.value)))
    
    def on_text_validate(self,widget):
        self.text_input_str = widget.text



class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        
        for i in range(0,50):
            b = Button(text = str(i + 1),size_hint=(None, None),size=(dp(100),dp(100)))
            self.add_widget(b)
    pass



class BoxLayoutExample(BoxLayout):
    pass
    # **kwargs allows us to pass a variable 
    # keyword arguments to a python function
"""    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        b1 = Button(text = 'A') 
        b2 = Button(text = 'B')
        b3 = Button(text = 'C') 

        self.add_widget(b2)
        self.add_widget(b1) 
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2)
            Color(0,1,0)
            Line(circle= (700,500,150), width=2)
            Line(rectangle= (700,500,150,100), width=2)
            self.rect = Rectangle(pos=(700,200), size=(150, 100))

    def on_button_a_click(self):
        #print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width -(x+w)
        if diff < inc:
            inc = diff
        
        x += inc

        x += dp(10)
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            self.ball =Ellipse(pos =(self.width / 2,self.height / 2) , size= (self.ball_size , self.ball_size))

        Clock.schedule_interval(self.update, 1/60)
    def on_size(self, *args):
        print("on size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = ((self.center_x - self.ball_size / 2),(self.center_y - self.ball_size / 2))
    
    def update(self, dt):
        #print("update!")
        x, y = self.ball.pos
        self.ball.pos = (x+4, y)



TheLabApp().run()
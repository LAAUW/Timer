import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols =1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Minutes :"))
        self.minutes = TextInput(multiline=False)
        self.inside.add_widget(self.minutes)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size = 40)
        self.submit.bind(on_press=self.confirmation)
        self.add_widget(self.submit)
    
    def reset(self, instance):
        self.minutes.text = ""

    def confirmation(self, instance):
        minutes = self.minutes.text

        self.add_widget(Label(text = "Shutdown in {0} minutes ! CONTINUE ?".format(minutes)))

        self.confirmation = GridLayout()
        self.confirmation.cols = 2

        self.yes_button = Button(text = "Yes", font_size = 40)
        self.yes_button.bind(on_press = self.shutdown)
        self.confirmation.add_widget(self.yes_button)

        self.no_button = Button(text = "No", font_size = 40)
        self.no_button.bind(on_press = self.reset)
        self.confirmation.add_widget(self.no_button)

        self.add_widget(self.confirmation)
    
    def shutdown(self, instance):
        minutes = self.minutes.text
        seconds = int(minutes)*60
        os.system('shutdown /s /t {0}'.format(seconds))


class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
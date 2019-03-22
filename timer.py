import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MainWindow(Screen):
    minutes = ObjectProperty(None)

    def validateMinutes(self):
        if self.minutes.text != "":
            ShutdownWindow.minutes = self.minutes.text
            self.minutes.text = ""

class ShutdownWindow(Screen):
    minutes = ""
    def shutdown(self):
        seconds = int(self.minutes) * 60
        print("Shutdown in minutes: ", self.minutes)
        os.system("shutdown /s /t {0}".format(seconds))

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("timer.kv")

class TimerApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    TimerApp().run()
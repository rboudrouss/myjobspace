# from kivymd.uix.gridlayout import GridLayout
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.label import MDLabel, MDIcon
# from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.list import ThreeLineListItem, MDList, ThreeLineIconListItem, IconLeftWidget, \
#     ThreeLineAvatarListItem, ImageLeftWidget
# from kivy.uix.scrollview import ScrollView
# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivy.uix.screenmanager import ScreenManager, Screen
# from helpers import *

from kivymd.app import MDApp
# from libs.baseclass
import os

class MyJobSpaceApp(MDApp):

    def __init__(self, **kwargs):
        # title
        self.title = "My Job Space"
        # theme
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.theme_style = 'Light'
        # other variables

        # super
        super().__init__(**kwargs)

    def build(self):
        return


if __name__ == "__main__":
    MyJobSpaceApp().run()

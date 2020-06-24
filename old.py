import kivy
from kivy.uix.label import Label #
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput #
from kivy.uix.button import Button #
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget  # le truc de base vide
from kivy.properties import ObjectProperty # pour récup l'id d'un object chez le fichier.kv
from kivy.graphics import Rectangle, Color, Line  # dessin \o/
from kivy.lang import Builder # convert txt => .kv file
from kivy.uix.screenmanager import ScreenManager, Screen   # pour changer d'écran
from kivy.app import App   # le truc de base base
from kivy.uix.popup import Popup   # un popup ;d
from kivy.uix.scatter import Scatter # pour faire bouger avec les clicks
from kivy.uix.boxlayout import BoxLayout # layout basic en box
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineListItem, MDList, ThreeLineIconListItem, IconLeftWidget, \
    ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
# from helpers import *

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First name :"))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name :"))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Email :"))
        self.mail = TextInput(multiline=False)
        self.inside.add_widget(self.mail)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)

        self.add_widget(self.inside)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print('pressed')
        name = self.name.text
        last = self.lastname.text
        email = self.mail.text

        print(f'Name : {name}, last name : {last}, mail : {email}')
        self.name.text = ""
        self.mail.text = ""
        self.lastname.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()


## my.kv

"""
<ALayout>:

    name: name
    last : last
    email: email

    GridLayout:
        cols:1
        size : root.width-200, root.height-200
        pos : 100, 100

        GridLayout:
            cols:2

            Label :
                text : "Name :"

            TextInput :
                id : name
                multiline : False

            Label :
                text : "Last name :"

            TextInput :
                id : last
                multiline : False

            Label :
                text : "Email :"

            TextInput :
                id : email
                multiline : False

        Button :
            on_press : root.btn()
            text : "Submit"
"""

class ALayout(Widget):
    name = ObjectProperty(None)
    last = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name :", self.name.text, "last name : ", self.last.text, 'Email :', self.email.text)
        self.name.text = ''
        self.last.text = ''
        self.email.text = ''


class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print('down', touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print('move', touch)

    def on_touch_up(self, touch):
        print('up', touch)
        self.btn.opacity = 1

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 1, 1, mode='rgba')
            self.line = Line(points=[0, 0, 0, 0], width=5)
            Color(1, 0, 0, 1, mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(20, 20))
            Color(0, 1, 0, 1, mode='rgba')
            self.rect2 = Rectangle(pos=(0, 0), size=(20, 20))
            Color(0, 0, 1, 1, mode='rgba')
            self.rect3 = Rectangle(pos=(0, 0), size=(20, 20))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print('down', touch)

    def on_touch_move(self, touch):
        self.rect2.pos = touch.pos
        self.line.points = self.rect.pos+touch.pos
        print('move', touch)

    def on_touch_up(self, touch):
        self.rect3.pos = touch.pos
        print('up', touch)
        self.rect2.pos = (-20, -20)

"""
WindowManager:
    MainWindow:
    SecondWindow:

<MainWindow>:
    name: 'main'
    GridLayout:
        cols:1

        GridLayout:
            cols:2

            Label:
                text :'pwd :'

            TextInput:
                id:passw
                multiline : False

        Button:
            text: 'Submit'
            on_release:
                app.root.current = "second" if passw.text == "rboud" else "main"
                root.manager.transition.direction = "left"
                passw.text = ""

<SecondWindow>:
    name: 'second'
    Button:
        text:"Back"
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"
"""
class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv

"""
<Widgets>:
    Button:
        text:'press me'
        on_release: root.btn()
<P>:
    Label:
        text:"you pressed"
        size_hint:0.6,0.2
        pos_hint:{"x":0.2,"top":1}

    Button:
        text:"Press !"
        size_hint:0.8,0.2
        pos_hint:{"x":0.1,"y":0.1}
"""
class Widgets(Widget):
    def btn(self):
        show_popup()


class P(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show = P()

    popupw = Popup(title="fromage", content=show,size_hint=(None, None), size=(400, 400))
    popupw.open()


class DemoApp(MDApp):

    def __init__(self, **kwargs):
        # title
        self.title = "Ma premiere appli :D"
        # theme
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.theme_style = 'Dark'
        # other variables
        self.dialog = None
        self.username = None
        self.password = None
        self.sm = ScreenManager()
        # super
        super().__init__(**kwargs)

    def build(self):
        # screens
        screen1 = Screen(name="login")

        # l = GridLayout(cols=1)
        # label = MDLabel(text="fromage", halign='center', theme_text_color="Custom",
        #                 text_color=(0, 1, 0, 0.5), font_style='Caption',
        #                 pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # icon_label = MDIcon(icon='language-python', halign='center',
        #                     pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # l.add_widget(label)
        # l.add_widget(icon_label)
        # l.add_widget(MDFlatButton(text="fromage",
        # pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        # l.add_widget(MDRectangleFlatButton(text='fromage',
        #                                   pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        # username = MDTextField(text="enter id:", size_hint_x=None,
        #                        width=300, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        button = MDRectangleFlatButton(
            text="show",
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            on_release=self.show_data
        )
        self.username = Builder.load_string("""username_helper""")
        self.password = Builder.load_string("""password_helper""")

        screen1.add_widget(self.username)
        # screen1.add_widget(self.password)
        screen1.add_widget(button)

        self.sm.add_widget(screen1)

        # screen 2
        screen2 = Screen(name="list")
        scroll = ScrollView()
        list_view = MDList()

        items = [

            ThreeLineAvatarListItem(
                text="Item {}".format(i),
                secondary_text="Hello world",
                tertiary_text="text"
            ) for i in range(1, 21)

        ]
        for item in items:
            item.add_widget(ImageLeftWidget(source="fb.png"))
            list_view.add_widget(item)
        list_view.add_widget(
            MDRectangleFlatButton(
                text="show",
                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                on_release=self.change_dark)
            )
        scroll.add_widget(list_view)
        screen2.add_widget(scroll)
        self.sm.add_widget(screen2)
        return self.sm

    def show_data(self, obj):
        close_button = MDFlatButton(
            text="close",
            on_release=self.close_dialog
        )
        more_button = MDFlatButton(
            text="more",
            on_release=self.verif_usr
        )

        self.dialog = MDDialog(
            text=self.username.text if self.username.text is not "" else "Please enter username",
            title="Username Check",
            size_hint=(0.7, 1),
            buttons=[
                more_button,
                close_button
            ]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def verif_usr(self, obj):
        if self.username.text == "fromage":
            self.dialog.dismiss()
            self.sm.current = "list"
        else:
            self.dialog.text = "bad user"

    def change_dark(self,obj):
        self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == "Light" else 'Light'

# from kivy.uix.label import Label #
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput #
# from kivy.uix.button import Button #
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.widget import Widget  # le truc de base vide
# from kivy.properties import ObjectProperty # pour récup l'id d'un object chez le fichier.kv
# from kivy.graphics import Rectangle, Color, Line  # dessin \o/
# from kivy.lang import Builder # convert txt => .kv file
# from kivy.uix.screenmanager import ScreenManager, Screen   # pour changer d'écran
# from kivy.app import App   # le truc de base base
# from kivy.uix.popup import Popup   # un popup ;d
# from kivy.uix.scatter import Scatter # pour faire bouger avec les clicks
# from kivy.uix.boxlayout import BoxLayout # layout basic en box
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

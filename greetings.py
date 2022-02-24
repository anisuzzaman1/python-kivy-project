from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        # Define Window Layout
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.title = 'Greetins | Developed by Anisuzzaman'

        # add widgets to window
        self.window.add_widget(Image(source="logo.png"))

        self.greeting = Label(
            text="What's is your name? ",
            font_size=20,
            color='#00ffcc'
        )
        self.window.add_widget(self.greeting)

        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.user)

        self.button = Button(
            text="Hello",
            size_hint=(1, 0.5),
            bold=True,
            background_color="#00ffcc"
        )
        # self.button.bind(on_press =self.on_click())
        self.button.bind(on_press=self.on_click)
        self.window.add_widget(self.button)

        return self.window

    def on_click(self, instance):
        if len(self.greeting.text) > 0:  # if text is not empty
            self.greeting.text = "Hello " + self.user.text + "!"
        else:
            self.greeting.text = "Please Enter Your Name:"


if __name__ == "__main__":
    SayHello().run()

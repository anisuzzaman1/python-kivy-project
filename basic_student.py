# Import Liabrary ------------
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# ------------------------------


class StudentGrid(GridLayout):
    def __init__(self,**kwargs):
        super(StudentGrid, self).__init__()
        self.cols = 100

        # ----------- Text Box Widget -------------
        self.add_widget(Label(text="Student Name: "))
        self.s_name = TextInput(multiline=True)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks"))
        self.s_marks = TextInput(multiline=True)
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender"))
        self.s_gender = TextInput(multiline=True)
        self.add_widget(self.s_gender)
        # ----------------------------------------

        self.press = Button(text="Submit")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)


    def click_me(self,instance):
        print("Student Name:"+self.s_name.text+" Marks: "+self.s_marks.text+" Gender: "+self.s_gender.text)

class StudentApp(App):
    def build(self):
        return StudentGrid()


if __name__ == "__main__":
    StudentApp().run()
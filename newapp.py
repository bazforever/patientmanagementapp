import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs): #adding arguments
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Patient Name'))
        self.p_name = TextInput()
        self.add_widget(self.p_name)

        self.add_widget(Label(text='Patient Adress'))
        self.p_adress = TextInput()
        self.add_widget(self.p_adress)

        self.add_widget(Label(text='Patient Gender'))
        self.p_gender = TextInput()
        self.add_widget(self.p_gender)

        self.press = Button(text="Click me")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)
    def click_me(self, instance):
        print("Patient Name:", self.p_name.text)
        print("Patient Adress:", self.p_adress.text)
        print("Gender of the Patient:", self.p_gender.text)
        print("")

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()






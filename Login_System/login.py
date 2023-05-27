import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox

class LoginWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def validate_user(self):
        user = self.ids.username_field
        password = self.ids.password_field
        info = self.ids.info

        uname = user.text
        pword = password.text

        if uname == '' or pword == '':
            info.text = '[color=#FF3D57] Username and/or Password are required! [/color]'

        elif uname == "admin" and pword == "admin":
            info.text = '[color=#01C38E] Logged In Successfully![/color]'

        else: 
            info.text = '[color=#FF3D57] Incorrect Username and/or Password![/color]'

class LoginApp(App):
    def build(self):
        return LoginWindow()

if __name__=="__main__":
    LoginApp().run()
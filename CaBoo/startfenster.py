#: Author : 			Christian Sannemann
#: Erstellt am : 		18.06.2020
#: Zuletzt geändert: 	18.06.2020


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class LoginFenster(FloatLayout):
	pass


class CaBooApp(App):
	def build(self):
		return LoginFenster()



if __name__ == "__main__":
	caboo = CaBooApp()
	caboo.run()
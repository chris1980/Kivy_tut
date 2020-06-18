# Author: 			Christian Sannemann
#Erstellt am: 		18.06.2020
#Zuletzt geändert: 	18.06.2020

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MyGridLayout(GridLayout):
	pass


class EmbeddedLayoutApp(App):
	def build(self):
		return MyGridLayout()


if __name__ == "__main__":
	EmbeddedLayoutApp().run()
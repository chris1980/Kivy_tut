# Author: 			Christian Sannemann
# Erstellt am: 		20.06.2020
# Zuletzt geändert: 30.06.2020


from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window


class DiaShow(RelativeLayout):
	Window.size =(400,100)
	pass


class BilderApp(App):
	def build(self):
		return DiaShow()


if __name__ == "__main__":
	dia = BilderApp()
	dia.run()

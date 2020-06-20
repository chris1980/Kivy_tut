#: Author: 				Christian Sannemann
#: Erstellt am:			20.06.2020
#: Zuletzt geändert:	20.06.2020


from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout


class Mani(RelativeLayout):
	pass


class ManipulationApp(App):
	def build(self):
		return Mani()


if __name__ == "__main__":
	canvas_mani = ManipulationApp()
	canvas_mani.run()
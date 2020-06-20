#: Author: 				Christian Sannemann
#: Erstellt am: 		20.06.2020
#: Zuletzt geändert: 	20.06.2020


from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class Leinwand(RelativeLayout):
	pass


class BeispielCanvasApp(App):
	def build(self):
		return Leinwand()


if __name__ == "__main__":
	leinwand = BeispielCanvasApp()
	leinwand.run()

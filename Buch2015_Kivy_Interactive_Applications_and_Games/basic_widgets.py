#Author: 			Christian Sannemann
#Erstellt am: 		18.06.2020
#Zuletzt geändert:	18.06.2020


from kivy.app import App
from kivy.uix.widget import Widget


class MyWidget(Widget):
	pass


class BasicWidget(App):
	def build(self):
		return MyWidget()


if __name__ == "__main__":
	widgetapp = BasicWidget()
	widgetapp.run()
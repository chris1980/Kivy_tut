#Author: 			Christian Sannemann
#Erstellt am:		18.06.2020
#Geändert am: 		20.06.2020

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file("toolbox.kv")
Builder.load_file("zeichenbrett.kv")
Builder.load_file("optionen.kv")
Builder.load_file("statusbar.kv")
Builder.load_file("comicwidgets.kv")

class ComicCreator(AnchorLayout):
	pass

class ComicCreatorApp(App):
	def build(self):
		return ComicCreator()

if __name__ == "__main__":
	cc = ComicCreatorApp()
	cc.run()
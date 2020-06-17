#author : 				Christian Sannemann
#Erstellt am:			14.06.2020
#Zuletzt geändert am:	14.06.2020
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer
from kivy.lang import Builder





class main_widget(Widget):
	pass

class NavDrawerApp(App):
	def build(self):
		theme_cls = ThemeManager()
		return main_widget


if __name__ == "__main__":
	drawer = NavDrawerApp()
	drawer.run()
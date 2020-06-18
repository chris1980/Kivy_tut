#Author : 			Christian Sannemann
#Erstellt am : 		18.06.2020
#Zuletzt geändert: 	18.06.2020

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# Es gibt 8 verschiedene Layouts in Kivy:
	# Floatlayout: 		Organisiert die Widgets in proportionalen Koordinaten mit "size_hint" und "pos_hint"
	#					deren Werte zwischen 0 und 1 sind, abhängig von der Position des Fensters
	# RelativeLayout: 	Organisiert die Widget ähnlich wie das FloatLayout, aber abhängig vom
	#					Layout, nicht mehr vom Fenster
	# GridLayout: 		Widgets werden in einem Grid organisiert, Es muss mind. eine Eigenschaft definiert werden:
	#					"cols" für Spalten oder "rows" für Zeilen
	# BoxLayout:		Widgets werden in einer Zeile oder Spalte organisiert, abhängig davon ob die Eigenschaft
	#					"orientation" auf "horizontal" oder "vertical" steht
	# StackLayout:		Ähnlich dem Boxlayout, sollte der Platz nicht reichen, nutzt das Layout die nächste Zeile oder
	#					Spalte. Zusätzliche Eigenschaften kann man mit : rl -bt benennen, was in dem Fall die Reihen-
	#					folge benennt: von rechts nach links und von unten(bottom) nach oben(top)
	# ScatterLayout: 	funktioniert wie das RelativeLayout, erlaubt aber auch multitouch Eingaben wie z.b. für
	# 					rotieren, skalieren und ähnliches
	# PageLayout: 		Stapelt die Widgets aufeinander und kreiert einen MultipageEffekt, womit man durch die Seiten
	#					blättern kann. Normalerweise nutzt man dann pro Seite noch andere Layouts um dort die Widgets
	#					entsprechend zu organisieren


class FloatApp(App):
	def build(self):
		return FloatLayout()


if __name__ =="__main__":
	FloatApp().run()
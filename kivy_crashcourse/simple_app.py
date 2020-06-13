#Author:			Christian Sannemann
#Erstellt am:		13.06.2020



from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


class ScatterApp(App):
	def build(self):
		f = FloatLayout()
		s = Scatter()
		l =  Label(text="Hello!",
					font_size=150)

		f.add_widget(s)
		s.add_widget(l)

		return f

if __name__ == "__main__":
	ScatterApp().run()
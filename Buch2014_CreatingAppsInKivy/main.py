from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class AddLocationForm(BoxLayout):
	pass

class WeatherApp(App):
	def build(self):
		return AddLocationForm()

if __name__ == "__main__":
	wetter = WeatherApp()
	wetter.run()
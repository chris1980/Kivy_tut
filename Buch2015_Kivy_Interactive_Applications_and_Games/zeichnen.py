from kivy.app import App
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout

class ZeichenBrett(RelativeLayout):
	Window.size = (500, 300)
	pass

class ZeichnenApp(App):
	def build(self):
		return ZeichenBrett()

if __name__ == "__main__":
	ZeichnenApp().run()

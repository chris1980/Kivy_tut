#: Author: 				Christian Sannemann
#: Erstellt am: 		20.06.2020
#: Zuletzt geändert: 	20.06.2020

from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line

class BeweglichesWidget(RelativeLayout):
	def __init__(self, **kwargs):
			self.selected = None
			super(BeweglichesWidget, self).__init__(**kwargs)
	def on_touch_down(self, touch):
		if self.collide_point(touch.x,touch.y):
			self.select()
			return True
		return super(BeweglichesWidget, self).on_touch_down(touch)
	def select(self):
		if not self.selected:
			self.ix = self.center_x
			self.iy = self.center_y
			with self.canvas:
				self.selected = Line(rectanlge=(0,0,self.width,self.height),dash_offset=2)
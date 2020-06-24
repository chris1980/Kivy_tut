# Author: Christian Sannemann
# Erstellt am: 24.06.2020
# Zuletzt geändert: 24.06.2020

import kivy

import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
#from comicwidgets import StickMan, BeweglichesWidget


class ToolButton(ToggleButton):
	def on_touch_down(self, touch):
		ds = self.parent.drawing_space
		if self.state == "down" and ds.collide_point(touch.x, touch.y):
			(x,y) = ds.to_widget(touch.x, touch.y)
			self.draw(ds, x, y)
			return True
		return super(ToolButton, self).on_touch_down(touch)
	def draw(self, ds, x, y):
		pass

class ToolStickman(ToolButton):
	def draw(self, ds, x, y):
		sm = StickMan(width=48, height=48)
		sm.center = (x,y)
		ds.add_widget(sm)

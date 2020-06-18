#Author: 			Christian Sannemann
#Erstellt am: 		18.06.2020
#Zuletzt geänder: 	18.06.2020


from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class MyPageLayout(PageLayout):
	pass


class MyPage(App):
	def build(self):
		return MyPageLayout()

if __name__ == "__main__":
	MyPage().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock



class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PlayerPaddle(Widget):
    pass

class PongGame(Widget):
    ball = ObjectProperty(None)

    def on_touch_down(self, touch):

        if touch.x < self.width /2:
            self.player1.center_y = touch.y
        if touch.x > self.width /2:
            self.player2.center_y = touch.y


    def update(self, delta_time):
        self.ball.move()

        #Kollisionskontrolle für die Spielerbalken
        if self.ball.collide_widget(self.player1)or self.ball.collide_widget(self.player2):
            self.ball.velocity_x *=-1

        #Abfrage für Spielrand Oben/Unten
        if(self.ball.y <0)or(self.ball.top > self.height):
            self.ball.velocity_y *= -1

        #Abfrage für Spielrand Links/Rechts
        if(self.ball.x <0)or(self.ball.right > self.width):
            self.ball.velocity_x *= -1

    def start(self):
        self.ball.velocity_x = 5
        self.ball.velocity_y = 5


class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        game.start()
        return game


if __name__ == "__main__":
    pong = PongApp()
    pong.run()

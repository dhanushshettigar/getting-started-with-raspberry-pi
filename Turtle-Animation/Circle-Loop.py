#importing turtle module
import turtle

tt = turtle.Turtle()

radius = 50

for i in range(100):
    tt.circle(radius + i, 45)

turtle.done()
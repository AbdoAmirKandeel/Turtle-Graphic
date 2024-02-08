#imports
import colorsys
import turtle

#Windows
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')

#Speed
t.speed(1000)
n = 90
h = 10

#Circle
for i in range (360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)

#End

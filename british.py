# -* encoding: utf-8 *
# VIM 
# :set expandtab
# :set encoding=utf-8

import turtle
from math import *

UNIT=12
W=60*UNIT
H=30*UNIT

def tan2angle(x):
   return 180 * atan(x) / pi

def topleft(t, w=W, h=H):
    t.home()
    t.left(180)
    t.forward(w/2)
    t.right(90)
    t.forward(h/2)
    t.right(90)

def drawline(t, x0, y0, x1, y1):
   topleft(t)
   t.fd(x0*UNIT)
   t.rt(90)
   t.fd(y0*UNIT)
   t.lt(tan2angle((x1-x0)/(y1-y0)))
   t.pendown()
   t.fd(sqrt(pow(x1-x0, 2) + pow(y1-y0, 2)) * UNIT)
   t.penup()

def drawrect(t, x0, y0, x1, y1):
    topleft(t)
    t.fd(x0 * UNIT)
    t.rt(90)
    t.fd(y0 * UNIT)
    t.pendown()
    for _ in range(2):
        t.fd((y1 - y0) * UNIT)
        t.lt(90)
        t.fd((x1 - x0) * UNIT)
        t.lt(90)
    t.penup()

''' w  * h '''
def draw_flag(t, color='red',w=30,h=20):
    t.home()
    t.left(180)
    t.forward(w/2)
    t.right(90)
    t.forward(h/2)
    t.pendown()
    t.fill(True)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
      t.right(90)
      t.forward(w)
      t.right(90)
      t.forward(h)
    t.end_fill()
    t.penup()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("British")
wn.screensize(W, H)
tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(1)
tess.penup()

tess.speed(5)
draw_flag(tess, color='#fff',w=W,h=H)
tess.speed(0)

tess.color('grey')
drawline(tess, 0, 0, 60, 30)
drawline(tess, 60, 0, 0, 30)

drawline(tess, 1/sin(atan(0.5)), 0, 60, 30 - 1/sin(atan(2.0)))
drawline(tess, 2/sin(atan(0.5)), 0, 60, 30 - 2/sin(atan(2.0)))
drawline(tess, 3/sin(atan(0.5)), 0, 60, 30 - 3/sin(atan(2.0)))

drawline(tess, 0, 1/sin(atan(2.0)), 60 - 1/sin(atan(0.5)), 30)
drawline(tess, 0, 2/sin(atan(2.0)), 60 - 2/sin(atan(0.5)), 30)
drawline(tess, 0, 3/sin(atan(2.0)), 60 - 3/sin(atan(0.5)), 30)

drawline(tess, 60 - 1/sin(atan(0.5)), 0, 0, 30 - 1/sin(atan(2.0)))
drawline(tess, 60 - 2/sin(atan(0.5)), 0, 0, 30 - 2/sin(atan(2.0)))
drawline(tess, 60 - 3/sin(atan(0.5)), 0, 0, 30 - 3/sin(atan(2.0)))

drawline(tess, 60, 1/sin(atan(2.0)), 1/sin(atan(0.5)), 30)
drawline(tess, 60, 2/sin(atan(2.0)), 2/sin(atan(0.5)), 30)
drawline(tess, 60, 3/sin(atan(2.0)), 3/sin(atan(0.5)), 30)

drawrect(tess,0, 0, 25, 10)
drawrect(tess,0, 0, 27, 12)

drawrect(tess, 35, 0, 60, 10)
drawrect(tess, 33, 0, 60, 12)

drawrect(tess,0, 18, 27, 30)
drawrect(tess,0, 20, 25, 30)

drawrect(tess,33, 18, 60, 30)
drawrect(tess,35, 20, 60, 30)

wn.exitonclick()


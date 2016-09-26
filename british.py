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
   t.fd(x0)
   t.rt(90)
   t.fd(y0)
   t.lt(tan2angle((x1-x0)/(y1-y0)))
   t.pendown()
   t.fd(sqrt(pow(x1-x0, 2) + pow(y1-y0, 2)) * UNIT)
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
wn.exitonclick()


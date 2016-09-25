# -* encoding: utf-8 *
# VIM 
# :set expandtab
# :set encoding=utf-8

import turtle
from math import *

def get_pentagram_side(radius):
    return radius * cos(radians(54))/cos(radians(36))

UNIT=400
B=1.9*UNIT
A=1.0*UNIT
R=A/13*4/5/2
C=A*7/13
D=B*2/5

def draw_star(t,x, y):
        topleft(t)
        t.fd(D/12*x)
        t.rt(90)
        t.fd(C/10*y)
        t.rt(180)

        t.left(72)
        t.forward(R)
        t.right(162) # 位于五角星一个顶点
        t.color('white')
        t.pendown()
        t.begin_fill()
        for i in range(5):
            t.forward(get_pentagram_side(R))
            t.left(72)
            t.forward(get_pentagram_side(R))
            t.right(144)
        t.end_fill()
        t.penup()

def topleft(t, w=B, h=A):
    t.home()
    t.left(180)
    t.forward(w/2)
    t.right(90)
    t.forward(h/2)
    t.right(90)

def draw_strip(t, w=B, h=A):
    for i in range(7):
        topleft(t, w, h)
        t.rt(90)
        t.fd(i*h/13*2)
        t.lt(90)
        t.color('#B22234')
        t.pendown()
        t.begin_fill()
        for _ in range(2):
          t.forward(w)
          t.right(90)
          t.forward(h/13)
          t.right(90)
        t.end_fill()
        t.penup()

def draw_stars_rect(t, w=B, h=A):
    topleft(t, w, h)
    t.color('#3C3B6E')
    t.pendown()
    t.begin_fill()
    for _ in range(2):
      t.forward(w*2/5)
      t.right(90)
      t.forward(h*7/13)
      t.right(90)
    t.end_fill()
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
wn.title("USA")
wn.screensize(B, A)
tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(1)
tess.penup()

tess.speed(5)
draw_flag(tess, color='#fff',w=B,h=A)
tess.speed(0)
draw_strip(tess)
draw_stars_rect(tess)
for x in range(6):
    for y in range(5):
        draw_star(tess, 2*x+1, 2*y+1)
for x in range(5):
    for y in range(4):
        draw_star(tess, 2*x+2, 2*y+2)

wn.exitonclick()


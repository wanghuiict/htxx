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
   if y1 == y0:
       turn = 90
       if x1 < x0:
           turn += 180
   else:
       turn = tan2angle((x1-x0) * 1.0 /(y1-y0))
       if y1 < y0:
           turn += 180
   t.lt(turn)
   t.pendown()
   t.fd(sqrt(pow(x1-x0, 2) + pow(y1-y0, 2)) * UNIT)
   t.penup()

def drawlines(t, li, fill=False): 
    x0 = li[0][0]
    y0 = li[0][1]
    topleft(t)
    t.fd(x0 * UNIT)
    t.rt(90)
    t.fd(y0 * UNIT)

    if fill == True:
        t.begin_fill()
    for i in range(len(li) - 1):
       x0 = li[i][0]
       y0 = li[i][1]
       x1 = li[i+1][0]
       y1 = li[i+1][1]
       if y1 == y0:
           turn = 90
           if x1 < x0:
               turn += 180
       else:
           turn = tan2angle((x1-x0) * 1.0 /(y1-y0))
           if y1 < y0:
               turn += 180
       t.lt(turn)
       t.pendown()
       t.fd(sqrt(pow(x1-x0, 2) + pow(y1-y0, 2)) * UNIT)
       t.penup()
       t.rt(t.heading() + 90)
    if fill == True:
        t.end_fill()

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

tess.color('grey')
#drawline(tess, 10, 20, 30, 40)
#drawline(tess, 20, 10, 30, 40)
#drawline(tess, 20, 10, 5, 5)
#drawlines(tess, [(10,10),(10,20),(20,20),(20,10),(10,10)], True)

tess.speed(0)
drawline(tess, 0, 0, 60, 30)
drawline(tess, 60, 0, 0, 30)

# top-right
drawline(tess, 1/sin(atan(0.5)), 0, 60, 30 - 1/sin(atan(2.0)))
drawline(tess, 2/sin(atan(0.5)), 0, 60, 30 - 2/sin(atan(2.0)))
drawline(tess, 3/sin(atan(0.5)), 0, 60, 30 - 3/sin(atan(2.0)))

# bottom-left
drawline(tess, 0, 1/sin(atan(2.0)), 60 - 1/sin(atan(0.5)), 30)
drawline(tess, 0, 2/sin(atan(2.0)), 60 - 2/sin(atan(0.5)), 30)
drawline(tess, 0, 3/sin(atan(2.0)), 60 - 3/sin(atan(0.5)), 30)

# top-left
drawline(tess, 60 - 1/sin(atan(0.5)), 0, 0, 30 - 1/sin(atan(2.0)))
drawline(tess, 60 - 2/sin(atan(0.5)), 0, 0, 30 - 2/sin(atan(2.0)))
drawline(tess, 60 - 3/sin(atan(0.5)), 0, 0, 30 - 3/sin(atan(2.0)))

# bottom-right
drawline(tess, 60, 1/sin(atan(2.0)), 1/sin(atan(0.5)), 30)
drawline(tess, 60, 2/sin(atan(2.0)), 2/sin(atan(0.5)), 30)
drawline(tess, 60, 3/sin(atan(2.0)), 3/sin(atan(0.5)), 30)

# top-left
drawrect(tess,0, 0, 25, 10)
drawrect(tess,0, 0, 27, 12)

# top-right
drawrect(tess, 35, 0, 60, 10)
drawrect(tess, 33, 0, 60, 12)

# bottom-left
drawrect(tess,0, 18, 27, 30)
drawrect(tess,0, 20, 25, 30)

# bottom-right
drawrect(tess,33, 18, 60, 30)
drawrect(tess,35, 20, 60, 30)

tess.color('#CC0000')
tess.speed(5)
bigcross=[(27,0),(27,12),(0,12),(0,18),(27,18),(27,30),(33,30),
                (33,18),(60,18),(60,12),(33,12),(33,0),(27,0)]
drawlines(tess, bigcross, True)

top_left_band=[(0,0),(0, 2/sin(atan(2.0))),(2 * (10 - 2/sin(atan(2.0))), 10),(20,10),(0,0)]
drawlines(tess, top_left_band, True)

top_right_band=[(60,0),(60 - 2/sin(atan(0.5)), 0),(60-(20 + 2/sin(atan(0.5))), 10),(40,10),(60,0)]
drawlines(tess, top_right_band, True)

top_bottom_band=[(0,30),(2/sin(atan(0.5)), 30),(20 + 2/sin(atan(0.5)), 20),(20,20),(0,30)]
drawlines(tess, top_bottom_band, True)

bottom_right_band=[(60,30),(60, 30 - 2/sin(atan(2.0))),(60 -(20 - 2/sin(atan(0.5))), 20),(40,20),(60,30)]
drawlines(tess, bottom_right_band, True)

tess.color('#003399')
tri=[(0, 3/sin(atan(2.0))), (0, 10), (2 * (10 - 3/sin(atan(2.0))), 10), (0, 3/sin(atan(2.0)))]
drawlines(tess, tri, True)
tri=[(3/sin(atan(0.5)), 0), (25, 0), (25, (25 - 3/sin(atan(0.5)))/2), (3/sin(atan(0.5)), 0)]
drawlines(tess, tri, True)




wn.exitonclick()


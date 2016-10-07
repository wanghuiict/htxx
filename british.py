# -* encoding: utf-8 *
# VIM 
# :set expandtab
# :set encoding=utf-8

import turtle
from math import *

UNIT=12
W=60*UNIT
H=30*UNIT
x=1/sin(atan(0.5))
y=1/sin(atan(2.0))

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


def draw_helper_lines():
    drawline(tess, 0, 0, 60, 30)
    drawline(tess, 60, 0, 0, 30)
    
    # top-right
    drawline(tess, x, 0, 60, 30 - y)
    drawline(tess, 2*x, 0, 60, 30 - 2*y)
    drawline(tess, 3*x, 0, 60, 30 - 3*y)
    
    # bottom-left
    drawline(tess, 0, y, 60 - x, 30)
    drawline(tess, 0, 2*y, 60 - 2*x, 30)
    drawline(tess, 0, 3*y, 60 - 3*x, 30)
    
    # top-left
    drawline(tess, 60 - x, 0, 0, 30 - y)
    drawline(tess, 60 - 2*x, 0, 0, 30 - 2*y)
    drawline(tess, 60 - 3*x, 0, 0, 30 - 3*y)
    
    # bottom-right
    drawline(tess, 60, y, x, 30)
    drawline(tess, 60, 2*y, 2*x, 30)
    drawline(tess, 60, 3*y, 3*x, 30)
    
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

def draw_shapes():
    tess.color('#CC0000')
    bigcross=[(27,0),(27,12),(0,12),(0,18),(27,18),(27,30),(33,30),
                    (33,18),(60,18),(60,12),(33,12),(33,0),(27,0)]
    drawlines(tess, bigcross, True)
   
    stripes=[]
    stripes.append([(0,0),(0, 2*y),(2 * (10 - 2*y), 10),(20,10),(0,0)])
    stripes.append([(60,0),(60 - 2*x, 0),(60-(20 + 2*x), 10),(40,10),(60,0)])
    stripes.append([(0,30),(2*x, 30),(20 + 2*x, 20),(20,20),(0,30)])
    stripes.append([(60,30),(60, 30 - 2*y),(60 -(20 - 2*x), 20),(40,20),(60,30)])
    for stripe in stripes:
        drawlines(tess, stripe, True)
    
    tess.color('#003399')
    tri=[]
    tri.append([(0, 3*y), (0, 10), (2 * (10 - 3*y), 10), (0, 3*y)])
    tri.append([(3*x, 0), (25, 0), (25, (25 - 3*x)/2), (3*x, 0)])
    tri.append([(35,0), (60 - 3*x, 0), (35, (25 - 3*x)/2), (35,0)])
    tri.append([(60, 3*y), (60, 10), (60 - 2 * (10 - 3*y), 10), (60, 3*y)])
    tri.append([(0, 30 - 3*y), (0, 20), (2 * (10 - 3*y), 20), (0, 30 - 3*y)])
    tri.append([(3*x, 30), (25, 30), (25, 30 - (25 - 3*x)/2), (3*x, 30)])
    tri.append([(35,30), (60 - 3*x, 30), (35, 30 - (25 - 3*x)/2), (35,30)])
    tri.append([(60, 30 - 3*y), (60, 20), (60 - 2 * (10 - 3*y), 20), (60, 30 - 3*y)])
    for triangle in tri:
        drawlines(tess, triangle, True)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("British")
wn.screensize(W, H)
tess = turtle.Turtle()
tess.hideturtle()
tess.penup()

# delay some
'''
tess.speed(1)
for _ in range(10):
  tess.home()
  tess.fd(200)
'''

tess.speed(5)
tess.pensize(1)
draw_flag(tess, color='#fff',w=W,h=H)

tess.pensize(1)
tess.color('grey')
tess.speed(5)
draw_helper_lines()
draw_shapes()

tess.color('white')
tess.speed(0)
draw_helper_lines()
draw_shapes()

wn.exitonclick()

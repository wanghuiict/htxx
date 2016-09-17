# -* encoding: utf-8 *
# VIM 
# :set expandtab
# :set encoding=utf-8

import turtle
from math import *


UNIT=30 #24
W=60
H=40
R=2.75


''' w steps * h steps'''
def draw_flag(t, step, color='red',w=30,h=20):
    t.home()
    t.left(180)
    t.forward(w/2 * step)
    t.right(90)
    t.forward(h/2 * step)
    t.pendown()
    t.fill(True)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
      t.right(90)
      t.forward(w * step)
      t.right(90)
      t.forward(h * step)
    t.end_fill()
    t.penup()

def draw_grid_lines(t, step, color='lightgrey', w=300, h=200, centerx=0, centery=0):
    t.pensize(1)
    t.color(color)
    h = h / step
    w = w / step
    ts = [t]
    t.home()
    t.forward(w/2 * step)
    t.right(90)
    t.forward(h/2 * step)
    t.left(180) # right-bottom
    for i in range(h):
	c = t.clone()
        c.forward(i * step)
	ts.append(c)
    for x in ts:
        x.left(90)
        x.pendown()
        x.forward(w * step)
        x.penup()
    t.home()
    t.fd(w/2 * step)
    t.rt(90)
    t.fd(h/2 * step)
    t.rt(90)
    ts = [t]
    for i in range(w):
	c = t.clone()
        c.forward(i * step)
        ts.append(c)
    for x in ts:
        x.right(90)
        x.pendown()
        x.forward(h * step)
        x.penup()
    

def draw_five_rings(tess,showspace=True):
    # balck
    tess.penup()
    tess.home()
    tess.fd(R * UNIT)
    tess.lt(90)
    tess.pensize(0.5 * UNIT)
    #tess.pendown()
    tess.color('#232223')
    tess.circle(R * UNIT, 45)
    tess.pendown()
    tess.circle(R * UNIT, 180)
    tess.penup()
    tess.circle(R * UNIT, 45)
    tess.pendown()
    tess.circle(R * UNIT, 45)
    
    # red 
    tess.penup()
    tess.home()
    tess.fd((6.4 + R) * UNIT)
    tess.lt(90)
    tess.color('#EE324E')# 238,50,78)
    tess.pensize(0.5 * UNIT)
    tess.pendown()
    tess.circle(R * UNIT, 225)
    
    #  blue bottom
    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd((6.4 + R) * UNIT)
    tess.lt(90)
    tess.color('#0081BC') #0,129,188)
    tess.pendown()
    tess.circle(R * UNIT, 120)
   
    # yellow
    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd((3.2 + R) * UNIT)
    tess.lt(90)
    tess.fd(3 * UNIT)
    tess.pendown()

    if showspace == True:
        tess.color('white')
        tess.pensize(0.7 * UNIT)
        tess.circle(R * UNIT)
    tess.color('#FCB131') #252,177,49)
    tess.pensize(0.5 * UNIT)
    tess.circle(R * UNIT)
    
    # blue upper
    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd((6.4 + R) * UNIT)
    tess.rt(90)
    tess.pendown()

    if showspace == True:
        tess.color('white')
        tess.pensize(0.7 * UNIT)
        tess.circle(-R * UNIT, 240)
        tess.color('#0081BC') #0,129,188)
        tess.pensize(0.5 * UNIT)
        tess.circle(-R * UNIT, 5)
        tess.rt(180)
        tess.circle(R * UNIT, 240+10)
    else:
        tess.color('#0081BC') #0,129,188)
        tess.pensize(0.5 * UNIT)
        tess.circle(-R * UNIT, 240)
   
    # green
    tess.penup()
    tess.home()
    tess.fd((3.2 - R) * UNIT)
    tess.rt(90)
    tess.fd(3 * UNIT)
    tess.circle(R * UNIT, 135)
    tess.pendown()

    if showspace == True:
        tess.color('white')
        tess.pensize(0.7 * UNIT)
        tess.circle(R * UNIT, 180)
        tess.color('#009D57') #0,157,87)
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 5)
        tess.rt(180)
        tess.circle(-R * UNIT, 180+10)
    else:
        tess.color('#009D57') #0,157,87)
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 180)
   
    # black
    tess.penup()
    tess.home()
    tess.fd(R * UNIT)
    tess.lt(90)
    tess.pensize(0.5 * UNIT)
    tess.circle(R * UNIT, 225)
    tess.pendown()

    if showspace == True:
        tess.color('white')
        tess.pensize(0.7 * UNIT)
        tess.circle(R * UNIT, 45) # core work
        tess.color('#232223')
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 5)
        tess.rt(180)
        tess.circle(-R * UNIT, 45+10)
        tess.penup()
        tess.rt(180)
    else:
        tess.color('#232223')
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 45)
    tess.circle(R * UNIT, 90)
    tess.pendown()

    if showspace == True:
        tess.color('white')
        tess.pensize(0.7 * UNIT)
        tess.circle(R * UNIT, 90)
        tess.pensize(0.5 * UNIT)
        tess.color('#232223') #(35,34,35)
        tess.circle(R * UNIT, 5)
        tess.rt(180)
        tess.circle(-R * UNIT, 90+10)
    else:
        tess.pensize(0.5 * UNIT)
        tess.color('#232223') #(35,34,35)
        tess.circle(R * UNIT, 90)

    # green
    tess.penup()
    tess.home()
    tess.fd((3.2 - R) * UNIT)
    tess.rt(90)
    tess.fd(3 * UNIT)
    tess.color('#009D57') #0,157,87)
    tess.rt(180)
    tess.circle(-R * UNIT, 45)
    tess.rt(180)
    tess.pendown()
    ##
    if showspace == True:
        tess.color('white')
        tess.pensize(0.7 * UNIT)
        tess.circle(R * UNIT, 180)
        tess.color('#009D57') #0,157,87)
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 5)
        tess.rt(180)
        tess.circle(-R * UNIT, 180+10)
    else:
        tess.color('#009D57') #0,157,87)
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 180)
  
    # red
    tess.penup()
    tess.home()
    tess.fd((6.4 + R) * UNIT)
    tess.lt(90)
    tess.circle(R * UNIT, 225)
    tess.pendown()

    if showspace == True:
        tess.color('white')# 238,50,78)
        tess.pensize(0.7 * UNIT)
        tess.circle(R * UNIT, 135)
        tess.color('#EE324E')# 238,50,78)
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 5)
        tess.rt(180)
        tess.circle(-R * UNIT, 135+10)
    else:
        tess.color('#EE324E')# 238,50,78)
        tess.pensize(0.5 * UNIT)
        tess.circle(R * UNIT, 135)

def draw_outer_circles(tess,color='grey'):
    tess.pensize(2)
    tess.color(color)
    tess.penup()
    tess.home()
    tess.fd(3 * UNIT)
    tess.lt(90)
    tess.pendown()
    tess.circle(3 * UNIT)
    
    tess.penup()
    tess.home()
    tess.fd(9.4 * UNIT)
    tess.lt(90)
    tess.pendown()
    tess.circle(3 * UNIT)
    
    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd(3.4 * UNIT)
    tess.rt(90)
    tess.pendown()
    tess.circle(3 * UNIT)
    
    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd(6.2 * UNIT)
    tess.lt(90)
    tess.fd(3 * UNIT)
    tess.pendown()
    tess.circle(3 * UNIT)
    
    tess.penup()
    tess.home()
    tess.fd(0.2 * UNIT)
    tess.rt(90)
    tess.fd(3 * UNIT)
    tess.pendown()
    tess.circle(3 * UNIT)

def draw_inner_circles(tess,color='grey'):
    tess.pensize(2)
    tess.color(color)
    tess.penup()
    tess.home()
    tess.fd(2.5 * UNIT)
    tess.lt(90)
    tess.pendown()
    tess.circle(2.5 * UNIT)
    
    tess.penup()
    tess.home()
    tess.fd((9.4-0.5) * UNIT)
    tess.lt(90)
    tess.pendown()
    tess.circle(2.5 * UNIT)
    
    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd((3.4+0.5) * UNIT)
    tess.rt(90)
    tess.pendown()
    tess.circle(2.5 * UNIT)
    
    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd((6.2-0.5) * UNIT)
    tess.lt(90)
    tess.fd(3 * UNIT)
    tess.pendown()
    tess.circle(2.5 * UNIT)
    
    tess.penup()
    tess.home()
    tess.fd((0.2+0.5) * UNIT)
    tess.rt(90)
    tess.fd(3 * UNIT)
    tess.pendown()
    tess.circle(2.5 * UNIT)

def draw_short_line(t):
    oldspeed = t.speed()
    t.speed(0)

    t.penup()
    t.rt(90)
    t.fd(5)
    t.rt(180)
    t.pendown()
    t.fd(10)
    t.penup()
    t.rt(180)
    t.fd(5)
    t.lt(90)

    t.speed(oldspeed)

def draw_helper_lines(color='grey'):
    tess.color(color)
    tess.penup()
    tess.pensize(1)
    tess.home()
    draw_short_line(tess)
    tess.rt(180)
    tess.fd(3 * 3.2 * UNIT)
    tess.pendown()
    tess.rt(180)

#   for x in range(6):
#       draw_short_line(tess)
#	tess.pendown()
#	tess.fd(3.2 * UNIT)
#    draw_short_line(tess)
#    #tess.fd(20 * UNIT)

    for x in range(3):
	tess.pendown()
	tess.fd(0.2 * UNIT)
        draw_short_line(tess)
	tess.pendown()
	tess.fd(3 * UNIT)
        draw_short_line(tess)
	tess.pendown()
	tess.fd(3 * UNIT)
        draw_short_line(tess)
	tess.pendown()
	tess.fd(0.2 * UNIT)

#    draw_short_line(tess)
    #tess.fd(20 * UNIT)


    tess.penup()
    tess.home()
    tess.fd(3.2 * UNIT)
    tess.rt(90)
    for x in range(2):
        draw_short_line(tess)
	tess.pendown()
	tess.fd(3 * UNIT)
    draw_short_line(tess)

    tess.penup()
    tess.home()
    tess.rt(180)
    tess.fd(3.2 * UNIT)
    tess.lt(90)
    for x in range(2):
        draw_short_line(tess)
	tess.pendown()
	tess.fd(3 * UNIT)
    draw_short_line(tess)


wn = turtle.Screen()

wn.bgcolor("lightgreen")
wn.title("Olympic rings")
wn.screensize(W*10, H*10)
tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(1)
tess.penup()

# delay some
'''
tess.speed(1)
for _ in range(10):
  tess.home()
  tess.fd(200)
'''

draw_flag(tess, 10, color='white',w=W,h=H)


tess.speed(0)
#draw_grid_lines(tess, 12, w=W*10, h=H*10)

tess.speed(3)
draw_helper_lines()
tess.speed(5)
draw_outer_circles(tess)
draw_inner_circles(tess)
draw_five_rings(tess,False)

tess.speed(0)
draw_helper_lines('white')
draw_outer_circles(tess,'white')
draw_inner_circles(tess,'white')
draw_five_rings(tess)

#tess.speed(0)
#draw_grid_lines(tess, 12, color='white', w=W*10, h=H*10)
#draw_five_rings(tess)

wn.exitonclick()


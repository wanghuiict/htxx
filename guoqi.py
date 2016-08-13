# -* encoding: utf-8 *
# VIM 
# :set expandtab
# :set encoding=utf-8

import turtle
import time
from math import *

def get_pentagram_side(radius):
    return radius * cos(radians(54))/cos(radians(36))

STEP = 24 # 单位长度
STAR = [] # 半径 边长 圆心x 圆心y 倾斜角
r = 3 * STEP # 大五角星外接圆半径
x = get_pentagram_side(r) # 大五角星边长
STAR.append((r, x, 10, 5, 0))
r = STEP # 四个小五角星外接圆半径
x = get_pentagram_side(r) # 小五角星边长
STAR.append((r, x, 5, 8, 90+180*atan(3.0/5.0)/pi))
STAR.append((r, x, 3, 6, 90+180*atan(1.0/7.0)/pi))
STAR.append((r, x, 3, 3, 90-180*atan(2.0/7.0)/pi))
STAR.append((r, x, 5, 1, 90-180*atan(4.0/5.0)/pi))

''' 30 steps * 20 steps'''
def draw_red_flag(t):
    t.home()
    t.left(180)
    t.forward(15 * STEP)
    t.right(90)
    t.forward(10 * STEP)
    t.pendown()
    t.fill(True)
    t.color("red")
    t.begin_fill()
    for _ in range(2):
      t.right(90)
      t.forward(30 * STEP)
      t.right(90)
      t.forward(20 * STEP)
    t.end_fill()
    t.penup()

def goto_star_center(t, x):
    t.home()
    t.left(180)
    t.forward(x[2]* STEP)
    t.right(90)
    t.forward(x[3] * STEP)

def draw_five_stars(t, fill=True):
    t.color("yellow")
    for d in STAR:
        goto_star_center(t, d)
        t.left(d[4])
        t.left(72)
        t.forward(d[0])
        t.right(162) # 位于五角星一个顶点
        t.pendown()
        if fill == True:
            t.begin_fill()
        for i in range(5):
            t.forward(d[1])
            t.left(72)
            t.forward(d[1])
            t.right(144)
        if fill == True:
            t.end_fill()
        t.penup()

def draw_five_circles(t, color='lightgrey'):
    t.color(color)
    for d in STAR:
        goto_star_center(t, d)
        if True:         
            t.right(90)
            t.forward(d[0])
            t.left(90)
            t.pendown()
            t.circle(d[0])
            t.penup()

# connect center of circle
def draw_coc_lines(t, color='lightgrey'):
    t.color(color)
    for d in STAR[1:]:
        goto_star_center(t, d)
        t.left(d[4])
        t.pendown()
        t.forward(sqrt(pow(d[2]-STAR[0][2], 2) + pow(d[3]-STAR[0][3], 2)) * STEP)
        t.penup()

def draw_grid_lines(t, color='lightgrey'):
    t.color(color)
    t.home()
    t.forward(15 * STEP)
    t.left(180)
    t.pendown()
    t.forward(30 * STEP)
    t.penup()

    t.home()
    t.left(90)
    t.forward(10 * STEP)
    t.left(180)
    t.pendown()
    t.forward(20 * STEP)
    t.penup()
    for i in range(10):
        t.home()
        t.left(90)
        t.forward(i * STEP)
        t.left(90)
        t.pendown()
        t.forward(15 * STEP)
        t.penup()
    for i in range(15):
        t.home()
        t.left(180)
        t.forward(i * STEP)
        t.right(90)
        t.pendown()
        t.forward(10 * STEP)
        t.penup()
    
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("国旗")
wn.screensize(30 * STEP, 20 * STEP)
tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(1)
tess.penup()

tess.speed(5)
draw_red_flag(tess)
tess.speed(10)
draw_grid_lines(tess)
tess.speed(4)
draw_five_circles(tess)
draw_coc_lines(tess)
tess.speed(9)
draw_five_stars(tess, fill=False)
tess.speed(0)
draw_grid_lines(tess, color='red')
draw_five_circles(tess, color='red')
draw_coc_lines(tess, color='red')
draw_five_stars(tess)

wn.exitonclick()


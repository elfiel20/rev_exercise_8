#This is the code for exercise 8 question 6
#The firs step is to import the proper modules etc.
import color

import pygame

import pygame_helper
import math

#The following is the code to prepare to
#and then open up a graphics window with the given dimensions color etc..

pygame.init()

width = 400

height = 300

win = pygame.display.set_mode((width, height))

win.fill(color.lightgray)

#dark grey circle drawing
#circle drawing dark grey
x = width*0.80
y = width//10
radius = height//12
pygame.draw.circle(win, color.darkgray, (x, y), radius)

#circle drawing for blue circle in left bottom quadrant of dark grey circle
x = x*0.9375
y = y*1.5

pygame.draw.circle(win, color.blue, (x, y), radius)


pygame.display.update()

pygame_helper.wait_for_click()
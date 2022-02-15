#This is the code for exercise 8 question 6
#The firs step is to import the proper modules etc.
import color

import pygame

import pygame_helper

#The following is the code to prepare to
#and then open up a graphics window with the given dimensions color etc..

pygame.init()

width = 400

height = 300

win = pygame.display.set_mode((width, height))

win.fill(color.lightgray)

#circle drawing dark grey
x = width*0.80
y = width//10
radius = height//12
pygame.draw.circle(win, color.darkgray, (x, y), radius)

#circle drawing for adjusted blue circle
x = x*0.90
y = y*2.25

pygame.draw.circle(win, color.blue, (x, y), radius)


pygame.display.update()

pygame_helper.wait_for_click()
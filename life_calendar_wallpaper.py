#!/usr/bin/env python
import math
import time
import os


start = [7, 5, 2001] # your birthday day/month/year
life_expectancy = 82 # how many year you are supposed to live

# your screen size
window_x = int(1920)
window_y = int(1080)



try:
    import pygame
except :
    os.system('python -m pip install pygame')

try:
    from wallpaper import set_wallpaper
except :
    os.system('python -m pip install py-wallpaper')

import pygame
from wallpaper import set_wallpaper

start[0] -= 1
start[1] -= 1
start[2] -= 1970
t_start = start[0]*24*60*60 + start[1]*365.25/12*24*60*60 + start[2]*365.25*24*60*60
t_end = t_start + life_expectancy*365*24*60*60
nb_weeks = life_expectancy*365/7
print(start, start, t_end)
weeks_len = 7*24*60*60

window = pygame.display.set_mode((window_x, window_y))


print("nb_weeks", nb_weeks)

size_x = int(nb_weeks**(0.5)*((window_x/window_y)**0.5))
size_y = int(nb_weeks**(0.5)*((window_y/window_x)**0.5))+1
print(size_x, size_y)

inc_x = window_x/(size_x+0.5)
inc_y = window_y/(size_y+0.5)
size = (inc_x+inc_y)/3
print("inc", inc_x, inc_y)



def generate_wall():
    n = 0
    actual = time.time()
    t = t_start
    for y in range(0, size_y):
        for x in range(0, size_x):
            pose_x = inc_x*x+inc_x/2
            pose_y = inc_y*y+inc_y/2
            #pygame.draw.rect(window, (150, 150, 150), (pose_x, pose_y, size, size))
            if actual > t:
                t += weeks_len
                pygame.draw.rect(window, (100, 0, 0), (pose_x+1, pose_y+1, size-2, size-2))
            else:
                pygame.draw.rect(window, (50, 50, 50), (pose_x+1, pose_y+1, size-2, size-2))
            n += 1
            if n > nb_weeks:
                return

generate_wall()

pygame.display.flip()
pygame.image.save(window, "screenshot.png")

set_wallpaper("screenshot.png")

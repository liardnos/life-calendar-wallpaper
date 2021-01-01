#!/usr/bin/env python
import math
import time
import os
import datetime

start = [7, 5, 2001] # your birthday day/month/year
life_expectancy = 80.8 # how many year you are supposed to live

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

weeks_len = 7*24*60*60
year_len = 365.25*24*60*60

start[0] -= 1
start[1] -= 1
start[2] -= 1970
t_start = start[0]*24*60*60 + start[1]*365.25/12*24*60*60 + start[2]*365.25*24*60*60
#print("dif ", (t_start % weeks_len)/weeks_len*7)
t_start -= t_start % weeks_len + weeks_len/7*3
t_end = t_start + life_expectancy*365.25*24*60*60
nb_weeks = life_expectancy*365.25/7
#print(start, start, t_end)



window = pygame.display.set_mode((window_x, window_y))
pygame.font.init()

#print("nb_weeks", nb_weeks)
# ~one year for each colum
size_y = 52                              + 6
size_x = int(nb_weeks/(52.1785714286))+1 + 6
"""
#auto size for current size
size_x = int(nb_weeks**(0.5)*((window_x/window_y)**0.5))   + 6
size_y = int(nb_weeks**(0.5)*((window_y/window_x)**0.5))+1 + 6
"""


#print(size_x, size_y)

inc_x = window_x/(size_x+0.5)
inc_y = window_y/(size_y+0.5)
size = min(inc_y/1.25, inc_x/1.25)
font = pygame.font.Font(pygame.font.get_default_font(), int(size-2))
#print("inc", inc_x, inc_y)

#for x in range(40):
    #print("#"*40)

def generate_wall():
    n = 0
    actual = time.time() + weeks_len
    t = t_start
    date_prev = date = datetime.datetime.fromtimestamp(t)
    for x in range(3, size_x-3):
        sprt = font.render(str(x-3), True, (75, 75, 75))
        sprt = pygame.transform.rotozoom(sprt, 45, 1)
        sprt_size = sprt.get_size()
        window.blit(sprt, (inc_x*x+inc_x/2+(size-2)/2-sprt_size[0]/2, inc_y*2))

        #for y in range(3, size_y+1-3):
        y = 3
        while 1:
            date = datetime.datetime.fromtimestamp(t)

            #print(date, date.strftime("%A"))
            pose_x = inc_x*x+inc_x/2
            pose_y = inc_y*y+inc_y/2
            t += weeks_len


            color = [0, 0, 0]
            if actual > t:
                color[0] += 200
            else:
                color = [25, 25, 25]
                if date.year != date_prev.year:
                    color = [25, 25, 25]
                    #print("year")

                elif date.month != date_prev.month:
                    color = [20, 20, 20]
                    #print("month")
            #print(color)
            #pygame.draw.rect(window, color, (pose_x+1, pose_y+1, size-2, size-2))
            if date.year != date_prev.year:
                if actual <= t:
                    color[0], color[1], color[2] = color[0]+50, color[1]+50, color[2]+50
                sprt = font.render(str(date.year), True, color)
                sprt = pygame.transform.rotozoom(sprt, 30, 1)
                sprt_size = sprt.get_size()
                window.blit(sprt, (pose_x+size/2-sprt_size[0]/2, pose_y-sprt_size[1]/2+size/2))

            elif date.month != date_prev.month:
                if actual <= t:
                    color[0], color[1], color[2] = color[0]+50, color[1]+50, color[2]+50
                sprt = font.render(str(date.month), True, color)
                sprt_size = sprt.get_size()
                window.blit(sprt, (pose_x+size/2-sprt_size[0]/2, pose_y-sprt_size[1]/2+size/2))

            else:
                if actual <= t:
                    color[0], color[1], color[2] = color[0], color[1], color[2]
                sprt = font.render(str(date.day), True, color)
                sprt_size = sprt.get_size()
                window.blit(sprt, (pose_x+size/2-sprt_size[0]/2, pose_y-sprt_size[1]/2+size/2))

            n += 1
            #end of the drawing
            if n > nb_weeks:
                return
            y += 1
            if (t-t_start) % year_len < weeks_len:
                date_prev = date
                break
            date_prev = date

generate_wall()

pygame.display.flip()
pygame.image.save(window, "screenshot.png")
set_wallpaper("screenshot.png")

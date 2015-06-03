import sys
import time
import pygame2
import pygame2.sdl.constants as constants
import pygame2.sdl.image as image
import pygame2.sdl.video as video
video.init()
img = image.load_bmp("c:\\test.bmp")
screen = video.set_mode(img.width, img.height)
screen.fill(pygame2.Color(255, 255, 255))
screen.blit(img, (0, 0))
screen.flip()
time.sleep(10)
import pygame
import random
import DisplayEmulator
import blob

width = 14
height = 14

de = DisplayEmulator.DisplayEmulator(width, height, 20)

background = (0, 0, 0)
white = (255, 255, 255)

frame = [[background] * width] * height
# for i in range(0, width):
#     line = [background] * width
#     for j in range(0, height):
#         line[j] = (i * 15, j * 6, i*j)
#     frame[i] = line
#
# de.pushFrame(frame)

while True:

    de.pushFrame(frame)

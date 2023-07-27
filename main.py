import pygame
import random
import DisplayEmulator
import blob
import roundArray

width = 18
height = 14
fadeThreshold = 0.8

de = DisplayEmulator.DisplayEmulator(width, height, 20)

background = (0, 0, 0)
white = (255, 255, 255)

frame = [[background] * height] * width

de.pushFrame(frame)
testBlob = blob.Blob(0, 0, (400, 100), 1)
testBlob2 = blob.Blob(0, 14, (400, -100), 1)

while True:
    fade = roundArray.RoundArray(width, height)
    fade = testBlob.addFade(fade)
    fade = testBlob2.addFade(fade)
    for i in range(0, width):
        line = [background] * width
        for j in range(0, height):
            if fade.get(i, j) >= fadeThreshold:
                line[j] = white
            else:
                line[j] = background
        frame[i] = line
    #print(fade.getArr())
    #print(frame)
    testBlob.updatePos()
    testBlob2.updatePos()
    de.pushFrame(frame)

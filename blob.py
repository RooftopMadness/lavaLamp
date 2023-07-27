import roundArray
import math

class Blob:
    def __init__(self, x, y, vel, size):
        self.posX = x
        self.posY = y
        self.vel = vel
        self.size = size
        self.margin = 5

    def updatePos(self):
        self.posX += self.vel[0]/1000
        self.posY += self.vel[1]/1000

    def addFade(self, fade):
        size = fade.getSize()
        for x in range(-self.margin,size[0]+self.margin):
            for y in range(-self.margin, size[1]+self.margin):
                power = 1/self.calcDis(x, y, size[0])
                fade.add(x, y, power)
        # x = round(self.posX)
        # y = round(self.posY)
        # fade.add(x, y, 1)
        return fade

    def calcDis(self, x, y, sizeX):
        x = x + 0.5
        y = y + 0.5
        return math.sqrt(((x-(self.posX % sizeX)) ** 2) + ((y - self.posY) ** 2))

import roundArray

class Blob:
    def __init__(self, x, y, vel, size):
        self.posX = x
        self.posY = y
        self.vel = vel
        self.size = size

    def updatePos(self):
        self.posX += self.vel[0]/1000
        self.posY += self.vel[1]/1000

    def addFade(self, fade):
        x = round(self.posX)
        y = round(self.posY)
        fade.add(x, y, 1)
        return fade


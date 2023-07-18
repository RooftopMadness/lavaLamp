class Blob:
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.vel = (0,0)
        self.size = 1

    def updatePos(self):
        self.posX += self.vel[0]
        self.posY += self.vel[1]

    def addFade(self, fade):
        
        return fade


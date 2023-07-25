class RoundArray:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[0.0]*sizeY]*sizeX

    def set(self, x, y, val):
        indexX = (x % self.sizeX)
        print(indexX)
        if y>self.sizeY:
            return False
        self.grid[indexX][y] = val
        return True

    def add(self, x, y, val):
        indexX = (x % self.sizeX)
        print(indexX)
        if y > self.sizeY:
            return False
        self.grid[indexX][y] = self.grid[indexX][y] + val
        return True

    def get(self, x, y):
        indexX = (x % self.sizeX)
        if y > self.sizeY:
            return -1.0
        return self.grid[indexX][y]

    def getArr(self):
        return self.grid

    def getHeight(self):
        return self.sizeY

class RoundArray:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[0 for i in range(sizeY)] for j in range(sizeX)]

    def set(self, x, y, val):
        indexX = (x % self.sizeX)
        print(indexX)
        if y>=self.sizeY:
            return False
        self.grid[indexX][y] = val
        return True

    def add(self, x, y, val):
        # #print(self.grid)
        # indexX = (x % self.sizeX)
        # if y > self.sizeY:
        #     return False
        # self.grid[indexX][y] = self.grid[indexX][y] + val
        # print(self.grid[indexX][y])
        # #print(self.grid)
        return self.set(x, y, self.get(x, y) + val)

    def get(self, x, y):
        indexX = (x % self.sizeX)
        if y >= self.sizeY:
            return 0
        return self.grid[indexX][y]

    def getArr(self):
        return self.grid

    def getSize(self):
        return (self.sizeX, self.sizeY)

    def getHeight(self):
        return self.sizeY

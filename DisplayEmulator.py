import pygame

class DisplayEmulator:
    def __init__(self, width, height, scale):
        self.width = width
        self.width = width
        self.height = height
        self.scale = scale

        delay = 100

        pygame.init()
        self.win = pygame.display.set_mode((width * scale, height * scale))
        self.screen = pygame.Surface((width, height))

        run = True
        black = (0, 0, 0)
        white = (255, 255, 255)
        self.screen.fill(black)

    def pushFrame(self, frame):
        #frame is a 2d array of colours in format (r, g, b)
        # check if game has quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        rect_width = 1
        rect_height = 1
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(self.screen, frame[x][y], (x, y, rect_width, rect_height))
                self.win.blit(pygame.transform.scale(self.screen, self.win.get_rect().size), (0, 0))
        pygame.display.update()
        pygame.time.delay(1)

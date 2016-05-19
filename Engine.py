import pygame

from World import World


# class Thing:
#
#     def __init__(self, xy, col):
#         super().__init__()
#         self.x, self.y = xy
#         self.width = 200
#         self.height = 200
#         self.colour = col
#         self.momentum = (0,0)
#
#
#
#     def draw(self, display):
#         pygame.draw.rect(display, BLACK, (self.x ,self.y, self.width, self.height), 0)
#
#     def move(self):
#         offsetX, offsetY = self.momentum
#         self.x += offsetX
#         self.y += offsetY

#############

pygame.init()           ## Init block
displayWidth = 800
displayHeight = 800

BLACK = (0,  0,  0)
WHITE = (255,255,255)
RED   = (255,0,  0)
BLUE  = (0,  0,  255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("My Game!")
clock = pygame.time.Clock()

## game objects
width_height = (15,15)

initBonkCount = 20
initZapCount = 5

world = World(width_height, initBonkCount, initZapCount, (displayWidth, displayHeight))

cycleCount = 0

cyclesPerSecond = 1
###########################

crashed = False
while not crashed:
     ## event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

                ## logic
    world.performCycle(cycleCount)
    ## draw stuff
    gameDisplay.fill(WHITE)
    world.draw(gameDisplay)
    ## end
    pygame.display.flip() ## redraw screen
    clock.tick(cyclesPerSecond) ## 1 cycle per second
    cycleCount += 1



pygame.quit()

quit()

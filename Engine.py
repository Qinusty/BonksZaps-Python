import pygame
import Graphing
from World import World
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--bonks", type=int, default=20)
parser.add_argument("--zaps", type=int, default=5)
parser.add_argument("--cycles", type=int, default=50)
args = parser.parse_args()

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
width_height = (50,50)

initBonkCount = args.bonks
initZapCount = args.zaps

world = World(width_height, initBonkCount, initZapCount, (displayWidth, displayHeight))

cycleCount = 0

cyclesPerSecond = 20
###########################

bonkFpsData = [[],[], []]

crashed = False
while cycleCount < args.cycles and not crashed:
    ## event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    ## logic
    start = pygame.time.get_ticks()
    world.performCycle(cycleCount)
    timeTook = pygame.time.get_ticks() - start
    print("Cycle " + str(cycleCount)+ ": took " + str(timeTook) + "ms")
    ## draw stuff
    gameDisplay.fill(WHITE)
    world.draw(gameDisplay)
    ## end
    pygame.display.flip() ## redraw screen
    clock.tick(cyclesPerSecond) ## 1 cycle per second
    cycleCount += 1

    bonkFpsData[0].append(cycleCount)
    bonkFpsData[1].append(timeTook)
    bonkFpsData[2].append(world.bonkTotal)

gameDisplay.fill(WHITE)

Graphing.graphData(bonkFpsData, gameDisplay, width_height)

pygame.display.flip()  ## redraw screen
clock.tick(cyclesPerSecond)  ## 1 cycle per second

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


pygame.quit()
quit()

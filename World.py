import pygame
from Being import *
from Room import Room

class World:

    def __init__(self, wh, numBonks, numZaps, dimensions):
        super().__init__()
        self.size = wh
        self.grid = []
        self.bonkTotal = 0
        self.zapTotal = 0
        self._initGrid(numBonks, numZaps)
        self.drawOffset = 20
        self.drawGap = 10
        self.boxSize = int(((dimensions[1] - (self.drawOffset * 2) - (wh[1] * self.drawGap)))  / wh[1])

    def _initGrid(self, numBonks, numZaps):
        for x in range(0, self.size[0]): ## adding cols
            col = []
            for y in range(0, self.size[1]): ## adding values
                col.append(Room(self, (x,y)))
            self.grid.append(col)

        for col in self.grid:
            for room in col:
                room.connectingRooms = self.getConnectingRoomsAt(room.position)

        ## random gen
        bonksCreated = 0
        zapsCreated = 0
        bonksComplete = False
        zapsComplete = False
        while not (bonksComplete and zapsComplete):
            bonksComplete = bonksCreated >= numBonks
            zapsComplete = zapsCreated >= numZaps
            if (not bonksComplete) and (not zapsComplete):
                ## bonk or zap
                if (rand.randint(0,1) == 0):
                    self.randomlyPlaceBeing(Bonk)
                    bonksCreated += 1
                else:
                    self.randomlyPlaceBeing(Zap)
                    zapsCreated += 1
            elif bonksComplete:
                self.randomlyPlaceBeing(Zap)
                zapsCreated += 1
            elif zapsComplete: ## zaps complete
                self.randomlyPlaceBeing(Bonk)
                bonksCreated += 1

    def performCycle(self, cycleCount):
        for col in self.grid:
            for room in col:
                for being in room.beings:
                    being.act(cycleCount)

        self.randomlyPlaceBeing(Bonk)
        self.bonkTotal += 1

    def randomlyPlaceBeing(self, T):
        x = rand.randint(0, (self.size[0] - 1))
        y = rand.randint(0, (self.size[1] - 1))
        if T == Bonk:
            self.grid[x][y].addBeing(Bonk("B" + str(self.bonkTotal),
                                          rand.choice([True, False]),
                                          self.grid[x][y], 0))
            self.bonkTotal += 1
        elif T == Zap:
            self.grid[x][y].addBeing(Zap("Z" + str(self.zapTotal),
                                         self.grid[x][y], 0))
            self.zapTotal += 1

    def draw(self, display):
        ## draw rects
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                rectX = self.drawOffset + (x * (self.boxSize + self.drawGap))
                rectY = self.drawOffset + (y * (self.boxSize + self.drawGap))
                colour = (0,0,0) ## black
                if self.grid[x][y].countType(Zap) > 0: ## if theres a zap
                    colour = (255,0,0) ## bright red
                else:
                    RB = 230 - (self.grid[x][y].countType(Bonk) * 20)
                    if RB < 0:
                        RB = 0
                    colour = (RB,230,RB) ## logic... nope, LESS OTHER COLOURS MORE GREEN

                pygame.draw.rect(display, colour, (rectX, rectY, self.boxSize, self.boxSize), 0)

    def getConnectingRoomsAt(self, xy):
        connectingRooms = []
        x = xy[0]
        y = xy[1]
        if x > 0:
            connectingRooms.append(self.grid[x - 1][y]) ## left
            if y > 0:
                connectingRooms.append(self.grid[x - 1][y - 1]) ## top left
            if y < self.size[1] - 1:
                connectingRooms.append(self.grid[x-1][y + 1]) ## bottom left
        if x < self.size[0] - 1:
            connectingRooms.append(self.grid[x + 1][y]) ## right
            if y > 0:
                connectingRooms.append(self.grid[x + 1][y - 1]) ## top right
            if y < self.size[1] - 1:
                connectingRooms.append(self.grid[x + 1][y + 1]) ## bottom right
        if y > 0:
            connectingRooms.append(self.grid[x][y - 1]) ## top
        if y < self.size[1] - 1:
            connectingRooms.append(self.grid[x][y + 1])

        return connectingRooms




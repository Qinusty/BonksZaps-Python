from Being import Bonk
import random as rand

class Room:

    def __init__(self, world,  xy):
        super().__init__()
        self.beings = []
        self.position = xy
        self.world = world
        self.connectingRooms = []

    def addBeing(self, being):
        self.beings.append(being)

    def addBabyBonk(self, currentCycle):
        self.addBeing(Bonk("B" + str(self.world.bonkTotal), rand.choice([True, False]), self, currentCycle))
        self.world.bonkTotal += 1

    def removeBeing(self, being):
        self.beings.remove(being)

    def countType(self, Type):
        counter = 0
        for being in self.beings:
            if isinstance(being, Type):
                counter += 1
        return counter


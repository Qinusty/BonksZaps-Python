from Being import Bonk
import random as rand

class Room:

    def __init__(self, world,  xy):
        super().__init__()
        self.beings = []
        self.position = xy
        self.world = world
        self.connectingRooms = []
        self.eligibleMales = []
        self.eligibleFemales = []

    def performCycle(self, cycleCount):
        self.eligibleFemales.clear()
        self.eligibleMales.clear()

        self.eligibleMales = list(filter(lambda b: isinstance(b, Bonk)
                                         and b.gender == True
                                         and b.eligibleToBreed(cycleCount), self.beings))
        self.eligibleFemales = list(filter(lambda b: isinstance(b, Bonk)
                                         and b.gender == False
                                         and b.eligibleToBreed(cycleCount), self.beings))
        for being in self.beings:
            being.act(cycleCount)

    def addBeing(self, being, currentCycle):
        self.beings.append(being)
        if isinstance(being, Bonk):
            if being.eligibleToBreed(currentCycle):
                if being.gender:
                    self.eligibleMales.append(being)
                else:
                    self.eligibleFemales.append(being)



    def addBabyBonk(self, currentCycle):
        self.addBeing(Bonk("B" + str(self.world.bonkTotal), rand.choice([True, False]), self, currentCycle), currentCycle)
        self.world.bonkTotal += 1

    def removeBeing(self, being):
        if isinstance(being, Bonk):
            if being.gender == True:
                if being in self.eligibleMales:
                    self.eligibleMales.remove(being)
            else:
                if being in self.eligibleFemales:
                    self.eligibleFemales.remove(being)
        self.beings.remove(being)

    def countType(self, Type):
        counter = 0
        for being in self.beings:
            if isinstance(being, Type):
                counter += 1
        return counter

    def __str__(self, *args, **kwargs):
        return str(self.position)




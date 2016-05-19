import random as rand

class Being:

    def __init__(self, name, room, currentCycle):
        super().__init__()
        self.room = room
        self.lastActed = currentCycle
        self.birthCycle = currentCycle
        self.lastReproduced = currentCycle
        self.name = name

        self.moveChance = 75

    def act(self, currentCycle):
        self.move()
        self.lastActed = currentCycle

    def move(self):
        if rand.randint(0, 100) > (100 - self.moveChance) and len(self.room.connectingRooms) > 0: ## 75% chance to move
            newRoom = rand.choice(self.room.connectingRooms) # inclusive random
            self.room.removeBeing(self)

            self.room = newRoom
            self.room.addBeing(self)



class Bonk(Being):

    def __init__(self, name, gender, room, currentCycle):
        super().__init__(name, room, currentCycle)
        self.gender = gender ## male

    def act(self, currentCycle):
        self.reproduce(currentCycle)

        super().act(currentCycle)

    def move(self):
        super().move()

    def reproduce(self, currentCycle):
        ## find appropriate mate
        for being in self.room.beings:
            if isinstance(being, Bonk) and being.gender != self.gender and being.eligibleToBreed(currentCycle):
                self.room.addBabyBonk(currentCycle)
                self.lastReproduced = currentCycle
                being.lastReproduced = currentCycle
                break

    def eligibleToBreed(self, currentCycle):
        if self.lastReproduced < currentCycle and self.birthCycle < currentCycle:
            return True
        else:
            return False

class Zap(Being):
    def __init__(self, name, room, currentCycle):
        super().__init__(name, room, currentCycle)

    def move(self):
        super().move()
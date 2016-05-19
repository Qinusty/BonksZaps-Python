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
        self.move(currentCycle)
        self.lastActed = currentCycle

    def move(self, currentCycle):
        if rand.randint(0, 100) > (100 - self.moveChance) and len(self.room.connectingRooms) > 0: ## 75% chance to move
            newRoom = rand.choice(self.room.connectingRooms) # inclusive random
            self.room.removeBeing(self)
            ## print(str(currentCycle) + " : " + self.name + " moved | " +  str(self.room) + " -> " + str(newRoom))
            self.room = newRoom
            self.room.addBeing(self, currentCycle)

            return True ## moved
        else:
            return False ## didnt move


    def __str__(self, *args, **kwargs):
        return self.name


class Bonk(Being):
    def __init__(self, name, gender, room, currentCycle):
        super().__init__(name, room, currentCycle)
        self.gender = gender ## male

    def act(self, currentCycle):
        if self.eligibleToBreed(currentCycle):
            self.reproduce(currentCycle)

        super().act(currentCycle)

    def move(self, currentCycle):
        super().move(currentCycle)

    def reproduce(self, currentCycle):
        ## find appropriate mate
        if self.gender == True:
            possibleMates = self.room.eligibleFemales
        else:
            possibleMates = self.room.eligibleMales

        for possibleMate in possibleMates:
            if possibleMate.room == self.room:
                mate = possibleMate
                if self.gender == True:
                    self.room.eligibleMales.remove(self)
                    self.room.eligibleFemales.remove(mate)
                else:
                    self.room.eligibleMales.remove(mate)
                    self.room.eligibleFemales.remove(self)
                self.room.addBabyBonk(currentCycle)
                self.lastReproduced = currentCycle
                mate.lastReproduced = currentCycle
                break

    def eligibleToBreed(self, currentCycle):
        if self.lastReproduced < currentCycle and self.birthCycle < currentCycle:
            return True
        else:
            return False

class Zap(Being):
    def __init__(self, name, room, currentCycle):
        super().__init__(name, room, currentCycle)

    def move(self, currentCycle):
        super().move(currentCycle)
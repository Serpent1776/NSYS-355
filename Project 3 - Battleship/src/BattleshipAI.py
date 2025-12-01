import random
from BattleshipGrid import BattleshipGrid
from BattleshipPoint import BattleshipPoint

#Note: may be revamped in 2026, depending on what Dr. Heinold's AI class contains. 
#This is really not an AI as I forsee, but what's your opinion?
class BattleshipAI:
    __foeCarrier = None
    __foeBattleship = None
    __foeSubmarine = None
    __foePatrolBoat = None
    __foesBoats = None
    __firstChoice = None
    __secondChoice = None
    __thirdChoice = None
    __fourthChoice = None
    __choices = None
    __misses = None
    __missIndex = None
    __hits = None
    __hitIndex = None
    __first = None
    __combo = None
    __spot = None
    __health = None
    __sameHits = None
    #0 is horizontal direction, 1 is vertical direction
    def __init__ (self, hostGrid): #initalizes the AI and randomly generates grid's ships
        self.__foeCarrier = list((5, random.randint(0,1)))
        self.__foeBattleship = list((4, random.randint(0,1)))
        self.__foeSubmarine = list((3, random.randint(0,1)))
        self.__foePatrolBoat = list((2, random.randint(0,1)))
        self.__foesBoats = list((self.__foeCarrier, self.__foeBattleship, self.__foeSubmarine, self.__foePatrolBoat))
        self.__firstChoice = random.randint(0,3)
        self.__secondChoice = random.randint(0,3)
        while(self.__secondChoice == self.__firstChoice):
            self.__secondChoice = random.randint(0,3)
        self.__thirdChoice = random.randint(0,3)
        while(self.__thirdChoice == self.__firstChoice or self.__thirdChoice == self.__secondChoice):
            self.__thirdChoice = random.randint(0,3)
        self.__fourthChoice = random.randint(0,3)
        while(self.__fourthChoice == self.__firstChoice or self.__fourthChoice == self.__secondChoice or self.__fourthChoice == self.__thirdChoice):
            self.__fourthChoice = random.randint(0,3)
        self.__choices = list((self.__firstChoice, self.__secondChoice, self.__thirdChoice, self.__fourthChoice))
        self.__misses = list(BattleshipPoint.__init_subclass__() for i in range(100))
        self.__missIndex = 0
        self.__hits = list(BattleshipPoint.__init_subclass__() for i in range(100))
        self.__hitIndex = 0
        self.__first = True
        self.__combo = 0
        self.__spot = None
        self.__health = 0
        self.__sameHits = 0
        forbiddenspots = list(str for i in range(64))
        fscounter = 0
        last = 0
        for i in self.__choices:
            if(last != 0):
                i = last
                last = 0
            fail = False
            spot = 0
            foeBoat = self.__foesBoats[i]
            spots = list(BattleshipPoint.__init_subclass__() for i in range(foeBoat[0]))
            if(i == self.__choices[0]):
                if(foeBoat[1] == 0): #horizontal
                    if(foeBoat[0] > 2):
                        spot = random.randint(0,9)*10 + random.randint(0, 9 - foeBoat[0])
                        spots[0] = hostGrid.findByNumber(spot)
                        spots[spots.__len__() - 1] = hostGrid.findByNumber(spot + foeBoat[0])
                        for u in range(1, foeBoat[0]):
                            spots[u] = hostGrid.findByNumber(spot + (u))
                    else:
                            spot = random.randint(0,9)*10 + random.randint(0, 9 - 1)
                            spots[0] = hostGrid.findByNumber(spot)
                            spots[1] = hostGrid.findByNumber(spot + 1)
                if(foeBoat[1] == 1): #vertical
                    if(foeBoat[0] > 2):
                        spot = random.randint(0,9 - foeBoat[0])*10 + random.randint(0, 9)
                        spots[0] = hostGrid.findByNumber(spot)
                        spots[spots.__len__() - 1] = hostGrid.findByNumber(spot + foeBoat[0]*10)
                        for u in range(1, foeBoat[0]):
                            spots[u] = hostGrid.findByNumber(spot + ((u)*10))
                    else:
                        spot = random.randint(0,9) + random.randint(0, 9 - 1)*10
                        spots[0] = hostGrid.findByNumber(spot)
                        spots[1] = hostGrid.findByNumber(spot + 10)
                for l in spots:
                    l.setShipPart()
                    forbiddenspots[fscounter] = l.getLocation()
                    fscounter += 1
                if(foeBoat[0] == 5):
                    hostGrid.setCarrier(spots)
                if(foeBoat[0] == 4):
                    hostGrid.setBattleship(spots)
                if(foeBoat[0] == 3):
                    hostGrid.setSubmarine(spots)
                if(foeBoat[0] == 2):
                    hostGrid.setPatrolBoat(spots)               
            if(i != self.__choices[0]):    
                if(foeBoat[1] == 0): #horizontal
                    if(foeBoat[0] > 2):
                        spot = random.randint(0,9)*10 + random.randint(0, 9 - foeBoat[0])
                        spots[0] = hostGrid.findByNumber(spot)
                        spots[spots.__len__() - 1] = hostGrid.findByNumber(spot + foeBoat[0])
                        while(spots[0].getLocation() in forbiddenspots or spots[spots.__len__() - 1].getLocation() in forbiddenspots):
                            spot = random.randint(0,9)*10 + random.randint(0, 9 - foeBoat[0])
                            spots[0] = hostGrid.findByNumber(spot)
                            spots[spots.__len__() - 1] = hostGrid.findByNumber(spot + foeBoat[0])
                        for u in range(1, foeBoat[0]):
                            spots[u] = hostGrid.findByNumber(spot + (u))
                            if(spots[u].getLocation() in forbiddenspots):
                                    fail = True
                                    break
                    else:
                        spot = random.randint(0, 9)*10 + random.randint(0, 9 - 1)
                        spots[0] = hostGrid.findByNumber(spot)
                        spots[1] = hostGrid.findByNumber(spot + 1)
                        while(spots[0].getLocation() in forbiddenspots or spots[1].getLocation() in forbiddenspots):
                            spot = random.randint(0,9)*10 + random.randint(0, 9 - 1)
                            spots[0] = hostGrid.findByNumber(spot)
                            spots[1] = hostGrid.findByNumber(spot + 1)                
                if(foeBoat[1] == 1): #vertical
                    if(foeBoat[0] > 2):
                        spot = random.randint(0, 9 - foeBoat[0])*10 + random.randint(0, 9)
                        spots[0] = hostGrid.findByNumber(spot)
                        spots[spots.__len__() - 1] = hostGrid.findByNumber(spot + foeBoat[0]*10)
                        while(spots[0].getLocation() in forbiddenspots or spots[spots.__len__() - 1].getLocation() in forbiddenspots):
                            spot = random.randint(0, 9 - foeBoat[0])*10 + random.randint(0, 9)
                            spots[0] = hostGrid.findByNumber(spot)
                            spots[spots.__len__() - 1] = hostGrid.findByNumber(spot + foeBoat[0]*10)
                        for u in range(1, foeBoat[0]):
                            spots[u] = hostGrid.findByNumber(spot + ((u)*10))
                            if(spots[u].getLocation() in forbiddenspots):
                                fail = True
                                break
                    else:
                        spot = random.randint(0,9) + random.randint(0, 9 - 1)*10
                        spots[0] = hostGrid.findByNumber(spot)
                        spots[1] = hostGrid.findByNumber(spot + 10)
                        while(spots[0].getLocation() in forbiddenspots or spots[spots.__len__() - 1].getLocation() in forbiddenspots):
                            spot = random.randint(0,9) + random.randint(0, 9 - 1)*10
                            spots[0] = hostGrid.findByNumber(spot)
                            spots[1] = hostGrid.findByNumber(spot + 10)
            if(fail == False):
                self.__health += foeBoat[0]
                for l in spots:
                    l.setShipPart()
                    forbiddenspots[fscounter] = l.getLocation()
                    fscounter += 1
                if(foeBoat[0] == 5):
                    hostGrid.setCarrier(spots)
                if(foeBoat[0] == 4):
                    hostGrid.setBattleship(spots)
                if(foeBoat[0] == 3):
                    hostGrid.setSubmarine(spots)
                if(foeBoat[0] == 2):
                    hostGrid.setPatrolBoat(spots)    
            else: #repeated the last part loop on cases where ships intersect each other
                i = last
                if(i == self.__choices[3]):
                    i = self.__choices[2]
                    last = 0

    def attack(self, clientGrid): #"attacks" a point from the client's grid
        point = None
        if(self.__first): #first case: random
            point = clientGrid.findByNumber(random.randint(0,99))
            if(point.isShipPart()):
                point.setHit()
                self.__hits[self.__hitIndex] = point
                self.__hitIndex += 1
            else:
                point.setMiss()
                self.__misses[self.__missIndex] = point
                self.__missIndex += 1
            self.__first = False
        elif((self.__hitIndex < 1 or self.__missIndex + self.__sameHits > self.__hitIndex*8) and self.__combo == 0): #default case: random
            while(point in self.__hits or point in self.__misses): 
                point = clientGrid.findByNumber(random.randint(0,99))
            if(point.isShipPart()): #only marks a hit when it hits a point that is a part of a ship.
                        point.setHit()
                        self.__hits[self.__hitIndex] = point
                        self.__hitIndex += 1
                        self.__combo += 1
            else:
                        point.setMiss()
                        self.__misses[self.__missIndex] = point
                        self.__missIndex += 1
                        self.__combo = 0
        else: #hit/combo case: hits a random adjacent point from the hit
                if self.__spot == None:
                    randNum = random.randint(0,3)
                    self.__spot = randNum
                if self.__spot == 0:
                    point = clientGrid.findByNumber(self.__hits[self.__hitIndex - 1].getIndex() + 1) #goes to an adjacent right point
                elif self.__spot == 1:
                    point = clientGrid.findByNumber(self.__hits[self.__hitIndex - 1].getIndex() + 10) #goes to an upward adjacent point
                elif self.__spot == 2:
                    point = clientGrid.findByNumber(self.__hits[self.__hitIndex - 1].getIndex() - 1) #goes to an adjacent left point
                elif self.__spot == 3:
                    point = clientGrid.findByNumber(self.__hits[self.__hitIndex - 1].getIndex() - 10) #goes to a downward adjacent point
                if(point in self.__hits):
                    self.__spot = None
                    self.__sameHits += 1
                    return self.attack(clientGrid) #recursion in cases where attack is a point that was already hit
                else:
                        self.__sameHits = 0
                if(point.isShipPart()):
                    point.setHit()
                    self.__hits[self.__hitIndex] = point
                    self.__hitIndex += 1
                    self.__combo += 1
                else:
                    point.setMiss()
                    self.__misses[self.__missIndex] = point
                    self.__missIndex += 1
                    self.__combo = 0
                    self.__spot = None
        return point
    
    def getHealth(self):
        return self.__health
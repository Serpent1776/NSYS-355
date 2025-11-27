from BattleshipPoint import BattleshipPoint
class BattleshipGrid:
    __2DArr = None
    __carrier = None
    __battleship = None
    __submarine = None
    __partolBoat = None
    def __init__(self):
        letters = list(str(chr(i)) for i in range(65,76))
        self.__2DArr = list(list(BattleshipPoint(letters[u] + str(i)) for i in range (1,11)) for u in range(0,11))
        self.__carrier = list()
        self.__battleship = list()
        self.__submarine = list()
        self.__partolBoat = list()
        a = 1

    def setCarrier(self, ship):
        self.__carrier = ship
    def setBattleship(self, ship):
        self.__battleship = ship
    def setSubmarine(self, sub):
        self.__submarine = sub
    def setPatrolBoat(self, boat):
        self.__partolBoat = boat
    def find(self, location):
        locations = {
            "A":0,
            "B":1,
            "C":2,
            "D":3,
            "E":4,
            "F":5,
            "G":6,
            "H":7,
            "I":8,
            "J":9
        }
        a = locations[location[0]]
        b = location[1:]
        return self.__2DArr[a][int(b) - 1]
    def findByNumber(self, location):
        if(location > 99):
            location = location - 100
            return self.__2DArr[location//10][location%10]
        elif(location > -1):
            return self.__2DArr[location//10][location%10]
        else:
            location = 100 + location
            return self.__2DArr[location//10][location%10]

    def __str__(self):
        store = "["
        for i in range(0,10):
            for u in range (0,10):
                store += str(self.__2DArr[i][u])
                if(i < 9 or u < 9):
                    store += ", "
            if(i < 9):
                store += "\n"
        return store + "]"
    
    def shipVision(self):
        store = "["
        for i in range(0,10):
            for u in range (0,10):
                if(self.__2DArr[i][u].isShipPart()):
                    store += str(self.__2DArr[i][u])
                else:
                    store += "  "
                if(i < 9 or u < 9):
                    store += ", "
            if(i < 9):
                store += "\n"
        return store + "]"
    
    def extractedString(self):
        store = ""
        for i in range(0,10):
            for u in range (0,10):
                    store += str(self.__2DArr[i][u])
                    if(not(i == 10 and u == 10)):
                        store += " "
        return store
    
    def eliminationVision(self):
        store = "["
        for i in range(0,10):
            for u in range (0,10):
                if(self.__2DArr[i][u].isShipPart()):
                    if(not self.__2DArr[i][u].isHitorMiss()):
                        store += str(self.__2DArr[i][u])
                    else:
                        store += "**"
                else:
                    store += "  "
                if(i < 9 or u < 9):
                    store += ", "
            if(i < 9):
                store += "\n"
        return store + "]"
    
    def attackVision(self):
        store = "["
        for i in range(0,10):
            for u in range (0,10):
                if(self.__2DArr[i][u].isShipPart() and self.__2DArr[i][u].isHitorMiss()):
                    store += str(self.__2DArr[i][u])
                else:
                    store += "  "
                if(i < 9 or u < 9):
                    store += ", "
            if(i < 9):
                store += "\n"
        return store + "]"
    
    def isCarrierSunk(self):
        for i in (self.__carrier):
            if(not i.isHitorMiss()):
                return False
        return True
    def isBattleshipSunk(self):
        for i in (self.__battleship):
            if(not i.isHitorMiss()):
                return False
        return True
    def isSubmarineSunk(self):
        for i in (self.__submarine):
            if(not i.isHitorMiss()):
                return False
        return True
    def isPatrolBoatSunk(self):
        for i in (self.__partolBoat):
            if(not i.isHitorMiss()):
                return False
        return True
    def findPointWithinShips(self, point):
        try:
            for i in(self.__carrier):
                if(i.equals(point)):
                    return "carrier"
        except:
            pass
        try:
            for i in(self.__battleship):
                if(i.equals(point)):
                    return "battleship"
        except:
            pass
        try:
            for i in(self.__submarine):
                if(i.equals(point)):
                    return "submarine"
        except:
            pass
        try:
            for i in(self.__partolBoat):
                if(i.equals(point)):
                    return "patrol boat"
        except:
            pass

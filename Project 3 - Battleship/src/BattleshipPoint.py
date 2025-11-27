class BattleshipPoint:
     __location = None
     __isShipPart = None
     __isHit = None
     __isMiss = None

     def __init__(self, location):
          self.__location = location
          self.__isShipPart = False
          self.__isHit = False
          self.__isMiss = False
     
     def __init_subclass__(self):
          self.__location = None
          self.__isShipPart = False
          self.__isHit = False
          self.__isMiss = False

     def setLocation(self, location):
          self.__location = location
     
     def getLocation(self):
          return self.__location

     def setShipPart(self):
          self.__isShipPart = True
     
     def setHit(self):
          self.__isHit = True
     def setMiss(self):
          self.__isMiss = True

     def __str__(self):
          return self.__location
     
     def sameLocationLetter(self, other):
          return self.__location[0] == other.__location[0]
     def sameLocationNum(self, other):
          return self.__location[1:] == other.__location[1:]
     def equals(self, other):
          return self.sameLocationLetter(other) and self.sameLocationNum(other)
     def letterToVertNum(self):
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
        return locations[self.__location[0]]
     def getIndex(self):
          return self.letterToVertNum() + (int(self.__location[1:])-1)
     def isShipPart(self):
          return self.__isShipPart
     def isHitorMiss(self):
          return self.__isHit and not self.__isMiss
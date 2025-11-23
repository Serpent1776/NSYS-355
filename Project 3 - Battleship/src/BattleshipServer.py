from BattleshipGrid import BattleshipGrid
from BattleshipPoint import BattleshipPoint
from BattleshipAI import BattleshipAI
from socket import *
import socket as ip
serverGrid = BattleshipGrid()
clientGrid = BattleshipGrid()
#print(serverGrid) #debug
ships = {
    2:5,
    3:4,
    4:3,
    5:2
}
serverPort = 7447
welcomeSocket = socket(AF_INET, SOCK_DGRAM) # create socket to allow connections
welcomeSocket.bind(('',serverPort)) # connect socket to port
print(ip.gethostbyname(ip.gethostname()))
playerHealth = 14
while True: # listen for connections forever
    msg, clientAddress = welcomeSocket.recvfrom(2048)
    print(clientGrid.extractedString())  #makes a string for UI purposes
    welcomeSocket.sendto((clientGrid.extractedString() + "\n").encode(), clientAddress)
    #print(msg.decode())
    for i in range(2,6):
        #welcomeSocket.sendto(("Make your " + ships[i] + "\n").encode(), clientAddress) note: null spam
        buildPoints, clientAddress = welcomeSocket.recvfrom(2048) #gets something like: from A1 to E1, from A1 to A5, from J10 to F10, or from F10 to F6
        print("Received: " + buildPoints.decode())
        start = clientGrid.find(buildPoints.decode().split(" ")[1])
        end = clientGrid.find(buildPoints.decode().split(" ")[3])
        if(start.sameLocationLetter(end)):
            if(int(str(start)[1:]) > int(str(end)[1:])):
                temp = end
                end = start
                start = temp
            shipList = list(BattleshipPoint.__init_subclass__() for u in range(ships[i]))
            index = 0
            for u in range(int(str(start)[1:]),int(str(end)[1:]) + 1):
                clientGrid.find(str(start)[0] + str(u)).setShipPart()
                shipList[index] =  clientGrid.find(str(start)[0] + str(u))
                index += 1
            if(i == 2):
                clientGrid.setCarrier(shipList)
            if(i == 3):
                clientGrid.setBattleship(shipList)
            if(i == 4):
                clientGrid.setSubmarine(shipList)
            if(i == 5):
                clientGrid.setPatrolBoat(shipList)

        if(start.sameLocationNum(end)):
            locations = {
            0:"A",
            1:"B",
            2:"C",
            3:"D",
            4:"E",
            5:"F",
            6:"G",
            7:"H",
            8:"I",
            9:"J"
        }
            if(start.letterToVertNum() > end.letterToVertNum()):
                temp = end
                end = start
                start = temp
            shipList = list(BattleshipPoint.__init_subclass__() for u in range(ships[i]))
            index = 0
            for u in range(start.letterToVertNum(), end.letterToVertNum() + 1):
                clientGrid.find(locations[u] + str(start)[1:]).setShipPart()
                shipList[index] =  clientGrid.find(locations[u] + str(start)[1:])
                index += 1
            if(i == 2):
                clientGrid.setCarrier(shipList)
            if(i == 3):
                clientGrid.setBattleship(shipList)
            if(i == 4):
                clientGrid.setSubmarine(shipList)
            if(i == 5):
                clientGrid.setPatrolBoat(shipList)
    
    welcomeSocket.sendto((clientGrid.shipVision() + "\n").encode(), clientAddress)
    commanderAI = BattleshipAI(serverGrid) #initalizes the "AI" and makes the server grid's ships 
    print(serverGrid.eliminationVision())
    #print("test works!")           
    #gameplay
    playing = True
    alreadySaidCarrierS = False
    alreadySaidCarrierC = False
    alreadySaidBattleshipS = False
    alreadySaidBattleshipC = False
    alreadySaidSubmarineS = False
    alreadySaidSubmarineC = False
    alreadySaidPatrolBoatS = False
    alreadySaidPatrolBoatC = False
    serverHealth = commanderAI.getHealth()
    while(playing):
        attack, clientAddress = welcomeSocket.recvfrom(2048) #gets attacked from a player-chosen coordinate
        hit = serverGrid.find(attack.decode())
        if(hit.isShipPart()):
            hit.setHit()
        else:
            hit.setMiss()
        point = commanderAI.attack(clientGrid)
        message = ""
        if(point.isHitorMiss()):
            message += "We hit you at " + point.getLocation() + "!\n"
            message += clientGrid.eliminationVision() + "\n"
            print(clientGrid.eliminationVision())
            playerHealth -= 1
        if(hit.isHitorMiss()):
            message += "You hit us at " + hit.getLocation() + "!\n"
            message += serverGrid.attackVision() + "\n"
            print(serverGrid.eliminationVision())
            serverHealth -= 1
        else:
            message += "You missed us at " + hit.getLocation() + "!\n"
        if(serverGrid.isCarrierSunk() and not alreadySaidCarrierC):
            message += "You sunk our Carrier!\n"
            alreadySaidCarrierC = True
        if(clientGrid.isCarrierSunk() and not alreadySaidCarrierS):
            message += "We sunk your Carrier!\n"
            alreadySaidCarrierS = True
        if(serverGrid.isBattleshipSunk() and not alreadySaidBattleshipC):
            message += "You sunk our Battleship!\n"
            alreadySaidBattleshipC = True
        if(clientGrid.isBattleshipSunk() and not alreadySaidBattleshipS):
            message += "We sunk your Battleship!\n"
            alreadySaidBattleshipS = True
        if(serverGrid.isSubmarineSunk() and not alreadySaidSubmarineC):
            message += "You sunk our Submarine!\n"
            alreadySaidSubmarineC = True
        if(clientGrid.isSubmarineSunk() and not alreadySaidSubmarineS):
            message += "We sunk your Submarine!\n"
            alreadySaidSubmarineS = True
        if(serverGrid.isPatrolBoatSunk() and not alreadySaidPatrolBoatC):
            message += "You sunk our Patrol Boat!\n"
            alreadySaidPatrolBoatC = True
        if(clientGrid.isPatrolBoatSunk() and not alreadySaidPatrolBoatS):
            message += "We sunk your PatrolBoat!\n"
            alreadySaidPatrolBoatS = True
        if(serverHealth < 1 or (serverGrid.isCarrierSunk() and serverGrid.isBattleshipSunk() and serverGrid.isSubmarineSunk() and serverGrid.isPatrolBoatSunk())):
            message += "You won against us!"
            playing = False
        if(playerHealth < 1 or (clientGrid.isCarrierSunk() and clientGrid.isBattleshipSunk() and clientGrid.isSubmarineSunk() and clientGrid.isPatrolBoatSunk())):
            message += "You lost against us!"
            playing = False
        welcomeSocket.sendto((message + "\n").encode(), clientAddress) 

    exit()
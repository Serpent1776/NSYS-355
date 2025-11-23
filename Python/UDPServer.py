#Server for processing strings, uses UDP
from socket import *
serverPort = 12001 # same port as client
serverSocket = socket(AF_INET, SOCK_DGRAM) # make the socket
serverSocket.bind(('', serverPort)) # make socket watch for appropriate traffic
while True: # wait for messages forever
    msg, clientAddress = serverSocket.recvfrom(2048) # get message from a client
    print('Received', msg)
    modmsg = msg.decode().upper() # convert message
    serverSocket.sendto(modmsg.encode(), clientAddress) # send back to client


from socket import *
serverPort = 13001
welcomeSocket = socket(AF_INET, SOCK_STREAM) # create socket to allow connections
welcomeSocket.bind(('',serverPort)) # connect socket to port
welcomeSocket.listen(1) # only 1 at a time
while True: # listen for connections forever
    connectionSocket, addr = welcomeSocket.accept() # create connection to client
    sentence = connectionSocket.recv(2048) # get message via connection
    print('Received:',sentence)
    capSentence = sentence.upper() # mess with message
    connectionSocket.send(capSentence) # send new message back to client
    connectionSocket.close()

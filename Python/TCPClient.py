from socket import *
serverName = '10.0.0.9' # address of server
serverPort = 13001 # port number for process
clientSocket = socket(AF_INET, SOCK_STREAM) # create a TCP socket
clientSocket.connect((serverName, serverPort)) # establish connection to server
sentence = input('Enter lowercase sentence: ').encode() # make string into bytes
clientSocket.send(sentence) # pass message to server
modSentence = clientSocket.recv(2048) # get message back from server
print('New sentence is:',modSentence.decode())
clientSocket.close() # shut down connection


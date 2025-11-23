# Client for sending messages via UDP
from socket import *
serverName = 'localhost' # server we're talking to
serverPort = 12001 # port name of server process
clientSocket = socket(AF_INET, SOCK_DGRAM) # make the UDP socket
message = input('Enter lowercase message:').encode() # get message as bytes
clientSocket.sendto(message, (serverName, serverPort)) # send message to server
modmessage, serverAddress = clientSocket.recvfrom(2048) # get new msg from server
print('Modified message:',modmessage.decode()) # convert to string and print
clientSocket.close() # shut down socket

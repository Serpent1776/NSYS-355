from socket import *
import time

serverName = 'localhost' # server we're talking to
serverPort = 12000 # port name of server process
clientSocket = socket(AF_INET, SOCK_DGRAM) # make the UDP socket
clientSocket.settimeout(3)
success = 1
for i in range(0 , 10):
    
    message = "ping " + str(success) + " time: " + time.asctime()
    message = message.encode() # get message as bytes
    startTime = time.time()
    clientSocket.sendto(message, (serverName, serverPort)) # send message to server
    try:
        modmessage, serverAddress = clientSocket.recvfrom(2048) # get new msg from server
        success += 1
        print(modmessage.decode()) # convert to string and print
        print("Round Trip Time:", time.time()-startTime) 
    except:
        print("Request Timed out")
    
clientSocket.close() # shut down socket

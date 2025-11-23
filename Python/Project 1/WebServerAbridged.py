# Import socket module
from socket import *    

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Finish creating server socket

# Place code here (10 points)
serverSocket.bind(('localhost', 12000))
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
	print('Ready to serve...')
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept() # Place code here (5 points)
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		message = connectionSocket.recv(2048) # Place code here (5 points)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		# print(filename[1:])
		f = open(filename[1:])
		# Store the entire content of the requested file in a temporary buffer
		outputdata = f.read() # place code here (5 points) 
		 # Send the HTTP response header line to the connection socket 
		connectionSocket.send("200 OK \n".encode()) # Place code here (10 points)     
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(bytes(outputdata[i],"utf-8"))
		connectionSocket.send(bytes("\r\n","utf-8"))
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		#print(IOError.with_traceback())
                # Fill in code here (10 points)
		connectionSocket.send("404 not found \n".encode())
		# Close the client connection socket
		connectionSocket.close()
		# Fill in code here (5 points)

serverSocket.close()  


#server.py file for CS164_Lab4
import socket
import sys
#for windows, import _thread
from thread import *

HOST = ''	#Symbolic name meaning all available interfaces
PORT = 5095 	#Arbitrary non-privlidged port

#Creates socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket Created')

try:	#binds a socket to a particular port
	s.bind((HOST, PORT))
except socket.error as msg:
	print('Bind Failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

print('Socket Bind Complete')

#Allows 10 connections to wait to be connected too
s.listen(10)
print('Socket now Listening')

#Now keep talking with the client
#Function for handling connections.
#This will be used to create threads.
def clientthread(conn):
	#Sending message to connected client
	#Send only takes string
	conn.send('Welcome to the server. Type something and hit enter\n')
	
	#Infinite loop so that function do not terminate and thread do not end.
	while True:
		s1 = "!q"
		s2 = "!sendall"
		#Receiving from client
		data = conn.recv(1024)
		if data[:2] == s1:
			print("ifONE")
			break
			#conn.close()
		elif data[:8] == s2:
			replyAll = data[8:]
			#print("ifTWO")
			for member in myList:
				print("ifTWO")#this is printing
				member.sendall(replyAll)
				#break; this one lets it keep running
			#break; this one made it disconnet immediately
		else:
			reply = 'OK...' + data
			if not data:
				break	
			conn.sendall(reply)

	#came out of loop
	conn.close()

#Now keep talking with the client
myList = []#you were redeclaring your list in the "while 1" loop
while 1:
	#Wait to accept a connection - blocking call
	#conn is the socket used for sending and recieving
	conn, addr = s.accept()
	member = conn
	#myList = []
	myList.append(member)
	print(len(myList))
	#display client information
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	#myList.append(member)
	#start new thread takes 1st argument as a function name to be run,
	#second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))
	#_thread.start_new_thread(clientthread ,(conn,))
s.close()

#Now keep talking with the client; NOW in the above loop
#data = conn.recv(1024)
#conn.sendall(data)	#send data over the connection we established
#conn.close()
#s.close()


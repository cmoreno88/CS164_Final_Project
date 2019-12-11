'''
	udp socket client
	Silver Moon
	sender
	https://www.binarytides.com/programming-udp-sockets-in-python/
'''
#originally UDP altered to implement RDT 3.0
# https://www.programiz.com/python-programming/time
# https://www.geeksforgeeks.org/time-functions-in-python-set-1-time-ctime-sleep/
import socket	# for sockets
import sys		# for exit
from getpass import getpass
# from check import ip_checksum
# import time
# import threading
# use it in this way
# https://www.bogotobogo.com/python/Multithread/python_multithreading_subclassing_Timer_Object.php

# create CLIENT dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()
###############################################################

# host = '10.0.0.4'
host = 'localhost';
port = 8888;
# seqnum = 0  # sequence number


rsp = raw_input("Welcome to Social. Please enter your username: ")
rflg = "1"
reply = rflg + rsp
s.sendto(reply, (host, port))

while 1:
	#	msg = 'Request menu'
	# msg = raw_input('Please Enter Password : ')

	try :
		d = s.recvfrom(1024)
		data = d[0]
		addr = d[1]
		rflg = data[0]			# response flag
	 	rsp = data[1:]			# response from the SERVER
		print rsp
		if rflg == "1":				# if the flag is 1 then we know that we have to ask for password		
			print rsp
			rsp = getpass()
			reply = rflg + rsp
			if raw_input("please press c to continue") == "c":
				s.sendto(reply, (host, port))
		elif rflg == "2":
			print rsp			# this is where the menu would be passed
			reply = "Here is my menu choice"
			if raw_input("please press c to continue") == "c":
				s.sendto(reply, (host, port))
		else:
			print rsp
			rsp = "Goodbye From Client"
			reply = rflg + rsp
			if raw_input("please press c to continue") == "c":
				s.sendto(reply, (host, port))
		# s.sendto(reply, (host, port))
		print'Server reply : '  + data
	
	# Handle exceptions
	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
#################################################################

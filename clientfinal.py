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
# create dgram udp socket

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

# host = '10.0.0.4'
host = 'localhost';
port = 8888;
# seqnum = 0  # sequence number



msg = raw_input("Welcome to Social. Please enter your username: ")
# chks = str(ip_checksum(msg))					#convert checksum return value to string
# changed the following for final lab
# data = (str(seqnum) + chks + msg)
# s.sendto(data, (host, port))
s.sendto(msg, (host, port))

while(1) :
#	msg = 'Request menu'
	# msg = raw_input('Please Enter Password : ')
	#chks = str(ip_checksum(msg))					#convert checksum return value to string
	#data = (str(seqnum) + chks + msg)				#all 3 values are strings and merged together
	try :
		# Set the whole string
		# s.sendto(data, (host, port))
		# s.sendto(msg, (host,port))
		# receive data from server (data, addr)
		d = s.recvfrom(1024)
		reply = d[0]
		addr = d[1]
		if reply == "pass":
			reply = getpass()
		else:
			reply = "goodbye"	
		# acknum = reply[0]								#we are recieving the acknowledge number
		# rchks = reply[1:3]
		# compchks = str(ip_checksum(reply[3:]))
		#check for ack, receive data from client (data, addr)
		#if not data: 
		#	break
		"""
		elif (str(seqnum) == acknum) and (rchks == compchks):		# verify seqnum/acknum and seqnum If good flip values
			newdata = 'clientAck and Sum Good'
			if seqnum == 0:
				seqnum = 1
			else:
				seqnum = 0
			# MAY need to move this assignment
			reply = (str(seqnum) + str(ip_checksum(newdata)) + newdata)
			#s.sendto(reply, (host, port))
			print 'Server reply : ' + newdata
		else:
			print 'clientAck and Sum Bad'
			reply = (str(seqnum) + chks + msg)
			#s.sendto(reply, (host, port))
			print 'Server reply : ' + msg
			"""
		s.sendto(reply, (host, port))
		print'Server reply : '  + reply
		
	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()

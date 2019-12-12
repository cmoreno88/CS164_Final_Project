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


def usrmsg():
	menu = {}
	menu['1'] = "1. ryan" 
	menu['2'] = "2. christopher"
	menu['3'] = "3. marcus"
	menu['4'] = "4. jacob"
	while True: 
	  options = menu.keys()
	  options.sort()	# dicts are inherently not sorted so we do this here
	  for entry in options: 
		  print menu[entry]
	  selection = raw_input("Please Select a User: ")
	  if selection == '1':
		  rcvr = "1"	# ryan
		  return rcvr
		  break
	  elif selection == '2':
		  rcvr = "2"	# christopher
		  return rcvr
		  break
	  elif selection == '3':
		  rcvr = "3"	# marcus
		  return rcvr
		  break
	  elif selection == '4':
		  rcvr = "4"	# jacob
		  return rcvr
		  break
	  else:
		  print "Please select valid user" 
	

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
rflg = "8"
tflg = "0"		# FRIEND flag
fflg = "0"			# FROM flag
reply = rflg + tflg + fflg + rsp
s.sendto(reply, (host, port))

while 1:
	#	msg = 'Request menu'
	# msg = raw_input('Please Enter Password : ')

	try :
		d = s.recvfrom(1024)
		data = d[0]
		addr = d[1]
		rflg = data[0]			# response flag
		tflg = data[1]
		fflg = data[2]
	 	rsp = data[3:]			# response from the SERVER
		# print rsp
		if rflg == "6":				# if the flag is 1 then we know that we have to ask for password		
			print rsp
			rsp = getpass()
			reply = rflg + tflg + fflg + rsp
			# if raw_input("please press c to continue") == "c":
			#	s.sendto(reply, (host, port))
			s.sendto(reply, (host, port))
		elif rflg == "7":
			print rsp			# this is where the menu would be passed
			reply = "Here is my menu choice"
			# if raw_input("please press c to continue") == "c":
			#	s.sendto(reply, (host, port))
			s.sendto(reply, (host, port))
		elif rflg == "1":
			print'Server reply : '  + rsp
			tflg = usrmsg() # sets friend flag
			print tflg
			rsp = raw_input("Enter message to send: ")
			reply = rflg + tflg + fflg + rsp
			s.sendto(reply, (host, port))
		else:
			print rsp
			rsp = "Goodbye From Client"
			reply = rflg + tflg + fflg + rsp
			if raw_input("please press c to continue") == "c":# stops looping
				s.sendto(reply, (host, port))
			#s.sendto(reply, (host, port))
		# print'Server reply : '  + rsp # data
	
# Handle exceptions #############################################
	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
#################################################################

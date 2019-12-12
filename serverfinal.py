'''
	Simple udp socket server
	reciever
	https://www.binarytides.com/programming-udp-sockets-in-python/
'''
#originally UDP altered to implement RDT 3.0
import socket
import sys
from check import ip_checksum
import time
from getpass import getpass

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port
# acknum = 0	# Created for acknowledgement number
users = dict({'ryan':'bently','christopher':'charlie','marcus':'shakes','jacob':'chopper'})
clients = dict()	# address dict for the clients
clientlist = []		# list to broadcast to all

def usrmsg(flg):
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
	  selection = flg # raw_input("Please Select a User: ")
	  if selection == '1':
		  rcvr = "ryan"
		  return rcvr
		  break
	  elif selection == '2':
		  rcvr = "christopher"
		  return rcvr
		  break
	  elif selection == '3':
		  rcvr = "marcus"
		  return rcvr
		  break
	  elif selection == '4':
		  rcvr = "jacob"
		  return rcvr
		  break
	  else:
		  print "Please select valid user" 


# Datagram (udp) socket ####################################
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
##########################################################

# Bind socket to local host and port ################################
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'
######################################################


#now keep talking with the client
while 1:
#	print 'loop check'						# receive data from client (data, addr)
	d = s.recvfrom(1024)					# Need to pull the seqnum and the checksum value
	data = d[0]
	addr = d[1]
	rflg = data[0]						# reponse flag
	tflg = data[1]					# friend flag
	fflg = data[2] 						# FROM flag
	rsp = data[3:]						# response from the CLIENT
	# print rsp
	if not data: 
		print 'break'
		break
	elif rsp in users.keys():
		print 'exist'
		curruser = rsp				# keep track of the current user
		print curruser
		if curruser == "ryan":
			fflg = "1"
		elif curruser == "christopher":
			fflg = "2"
		elif curruser == "marcus":
			fflg = "3"
		else:	# this has to be jacob
			fflg = "4"
		clients.update({curruser : addr})	# ADDS user & addr to client list
		print clients
		rflg = "6"
		# tflg = "0"
		rsp = "Please Enter Password: "
		reply = rflg + tflg + fflg + rsp
		s.sendto(reply , addr)
	elif rsp in users.values():
		print 'good pass'
		rsp = "welcome to Social!"
		rflg = "1"		# setting the flag to 1 enters messenger
		reply = rflg + tflg + fflg + rsp
		s.sendto(reply , addr)
	elif rflg == "1":			# This option sends messages
		# put a nested if in here to check if the message should go to 
		# another user or be broadcast?
		fromusr = usrmsg(fflg)		# who are we sending to?
		# print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + rsp # data.strip()
		addr = clients[fromusr]	# should set addr to send msg to
		rsp = "Please enter message: "
		reply = rflg + tflg + fflg + rsp
		s.sendto(reply , addr)
	else:
		print 'server else'
		print rsp
		rsp = "Goodbye from Server"
		rflg = "0"
		reply = rflg + tflg + fflg + rsp
		if raw_input("please press c to continue") == "c":
			s.sendto(reply , addr)
	# s.sendto(reply , addr)
	
	# MAY need to move this assignment
	# create an other dictionary that associates the USERNAME that connected
	# With the addr
#	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + rsp # data.strip()
	#########################################################
s.close()

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
"""
def usrmenu():
	menu = {}
	menu['1'] = "1. LogOut" 
	menu['2'] = "2. Change Password"
	# menu['3'] = "Send Message"
	while True: 
	  options = menu.keys()
	  options.sort()
	
	  for entry in options: 
		  print menu[entry]
		  
	  selection = raw_input("Please Select an Option number:")
	  if selection == '1':
		  print "logout" 
		  break
	  elif selection == '2':
		  print "change pwd"
	  else:
		  print "Unknown Option Selected!" 
	

def logon():	
	usrnm = raw_input("Welcome to Social. Please enter your username: ")
	pwd = getpass("Please enter your PassWord: ")

	print(usrnm + pwd)

	if usrnm in users:
		if users[usrnm] == pwd:
			print("welcome")
			usrmenu()
		else:
			print("no")
"""
HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port
# acknum = 0	# Created for acknowledgement number
users = dict({'ryan':'bently','christopher':'charlie','marcus':'shakes','jacob':'chopper'})

# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
##########################################################

# Bind socket to local host and port
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
	rsp = data[1:]						# response from the CLIENT
	print rsp
	if not data: 
		print 'break'
		break
	elif rsp in users.keys():
		print 'exist'
		rflg = "1"
		rsp = "Please Enter Password: "
		reply = rflg + rsp
		if raw_input("please press c to continue") == "c":
			s.sendto(reply , addr)
	elif rsp in users.values():
		print 'good pass'
		rsp = "welcome to Social!"
		rflg = "2"
		reply = rflg + rsp
		if raw_input("please press c to continue") == "c":
			s.sendto(reply , addr)
	else:
		print 'server else'
		rsp = "Goodbye from Server"
		rflg = "0"
		reply = rflg + rsp
		if raw_input("please press c to continue") == "c":
			s.sendto(reply , addr)
		# break
	# s.sendto(reply , addr)
	
	# MAY need to move this assignment
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
	#########################################################
s.close()

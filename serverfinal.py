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
import social

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


# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'

#now keep talking with the client
while 1:
#	print 'loop check'						# receive data from client (data, addr)
	d = s.recvfrom(1024)		# Need to pull the seqnum and the checksum value
	data = d[0]
	addr = d[1]
	# seqnum = data[0]
	# chks = data[1:3]
	# rchks = str(ip_checksum(data[3:]))
	
	if not data: 
		break
	# elif (seqnum == str(acknum)) and (chks == rchks):		#verify seqnum/acknum and seqnum If good flip values
	#	data = 'serverAck and Sum Good'
	#	reply = (str(acknum) + str(ip_checksum(data)) + data)
	#	if acknum == 0:
	#		acknum = 1
	#	else:
	#		acknum = 0
	#else:
	#	data = 'serverAck and Sum Bad'
	#	reply = (str(acknum) + str(ip_checksum(data)) + data)
	reply = 'ok...' + data
	s.sendto(reply , addr)
	# MAY need to move this assignment
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
	
s.close()

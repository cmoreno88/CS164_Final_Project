#Socket client example in python
import socket   #module for sockets
import sys      #module for exit

#create an AF_INET, STREAM socket (TCP)
#Function socket.socket creates a socket and returns a socket
#descriptor which can be used in other socket related functions
#Address Family: AF_INET (this is IP ver. 4 or IPv4
#Type: SOCK_STREAM (this means connection oriented TCP protocol)
#from Tools.scripts.which import msg

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#for error handling of socket creation failure
except socket.error as msg:
    print('Failed to create socket. Error: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()
print('Socket Created')

host = '10.0.0.4' #'www.google.com'; #
#host = 'en.wikipedia.org/wiki/Christopher';
port = 80   #port to connect to ip address of remote host/system
try:    #retrieves remote server host ip address and assigns it
    remote_ip = socket.gethostbyname(host)

except socket.gaierror: #could not resolve, cant return hostname
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('IP address of ' + host + ' is ' + remote_ip)

#Connect to remote server
s.connect((remote_ip, port))
print('Socket Connected to ' + host + ' on IP ' + remote_ip)
###########COULDNT GET THIS TO WORK############################
#send some data to remote server
#http command to fetch the mainoage of website
#message = "Get / HTTP/1.1\r\n\r\n"
message = 'GET / HTTP/1.1\r\n\r\n'

try:
#Set the whole string
	s.sendall(message)
except socket.error:
#Send failed
	print('Send Failed')
	sys.exit()

print('Message send successfully')

#Now recieve data
reply = s.recv(4096)

print(reply)
####################################################
s.close()


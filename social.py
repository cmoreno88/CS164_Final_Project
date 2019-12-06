from getpass import getpass	# 

users = dict({'ryan':'bently','christopher':'charlie','marcus':'shakes','jacob':'chopper'})


usrnm = raw_input("Welcome to Social. Please enter your username: ")
pwd = getpass("Please enter your PassWord: ")

print(usrnm + pwd)

if usrnm in users:
	if users[usrnm] == pwd:
		print("yes")
	else:
		print("no")
		
	
	

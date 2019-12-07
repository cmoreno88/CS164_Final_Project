from getpass import getpass	# 

users = dict({'ryan':'bently','christopher':'charlie','marcus':'shakes','jacob':'chopper'})

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
	
	
usrnm = raw_input("Welcome to Social. Please enter your username: ")
pwd = getpass("Please enter your PassWord: ")

print(usrnm + pwd)

if usrnm in users:
	if users[usrnm] == pwd:
		print("welcome")
		usrmenu()
	else:
		print("no")
		

	

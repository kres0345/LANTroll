Set objArgs = WScript.Arguments
Set wshShell = wscript.CreateObject("WScript.Shell")
keyboardtext = objArgs(0)
wscript.sleep 1000
wshshell.sendkeys keyboardtext

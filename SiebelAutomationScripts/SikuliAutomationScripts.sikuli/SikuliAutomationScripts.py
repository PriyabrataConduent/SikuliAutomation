import sys
import os

f=open("accounts.txt","r")
lines=f.readlines()
username=lines[0].rstrip('\n')
password=lines[1].rstrip('\n')
server=lines[2].rstrip('\n')
f.close()

#os.system('"D:\Siebel\8.1.1.16.0\Tools\BIN\siebdev.exe"')
vcCMD = '"D:\Siebel\8.1.1.16.0\Tools\BIN\siebdev.exe"'
App.open('CMD /C ' + vcCMD)
wait(2)
click("1533806419593.png")

#click("1533805805639.png")
#wait("Search.png")
#wait(1)
#type("Siebel Tools"+Key.ENTER)
wait(3)
wait("1533806419593.png")
wait("1533806623650.png")
type(username+Key.TAB)
wait("1533807033983.png")
type(password+Key.TAB)
wait(1)
type(server+Key.ENTER)
wait("1533872753866.png")
type(Key.ENTER)
wait(20)
wait("QSiebelTools.png", 200)
wait(20)







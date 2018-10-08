import sys
import os

login=open("accounts.txt","r")
lines=login.readlines()
username=lines[0].rstrip('\n')
password=lines[1].rstrip('\n')
server=lines[2].rstrip('\n')
login.close()

f=open("inputFile.txt","r")
lines=f.readlines()
objList=lines[0].rstrip('\n')
f.close()

click("1533805805639.png")
wait("Search.png")
type("Siebel Tools"+Key.ENTER)
wait(3)
wait("1533806419593.png")
wait(1)
wait("1533806623650.png")
type(username+Key.TAB)
wait("1533807033983.png")
type(password+Key.TAB)
type(server+Key.ENTER)
wait(20)
exists("1534416757603.png")
find("1534416801560.png")
wait(1)
click("applet.png")
wait(2)
type ("q",KeyModifier.CTRL)
wait("Name.png")
paste(objList)
type (Key.ENTER)
wait(2)
exists("ListObjectView.png")
keyDown(Key.SHIFT)
#click("1535239086318.png")
click("1535276628271.png")

wait(1)

#click("1534775267332.png")
#wait(1)
#keyDown(Key.CTRL)
#click("1534775287846.png")
#keyDown(Key.CTRL)
#click("1534775308189.png")
#keyDown(Key.CTRL)
#click("1534775334889.png")
rightClick("1535118531389.png")
exists("rightClick.png")
click("compile_selected_rightClick.png")
#type(Key.F7, KeyModifier.CTRL)
find("1534453184581.png")
wait(1)
wait("1534453234967.png")
click("1534453268029.png")
wait(3)
type("siebel_sia_08_16_2018.srf")
click("1534454073561.png")
wait("1534454164894.png")
click("1534454247270.png")
wait(50)
if exists("1534490859009.png"):
    wait("1534490884832.png")
    find("1534490902768.png")
    click("1534490939481.png")
    wait(2)
    wait("1534492161689.png")
    click("1534492179543.png")
elif exists("1534491998544.png"):
    wait("1534492064606.png")
    click("1534492092335.png")
else :
    wait("1534492161689.png")
    click("1534492179543.png")















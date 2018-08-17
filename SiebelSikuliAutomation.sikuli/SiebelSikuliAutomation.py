click("1533805805639.png")
wait("Search.png")
type("Siebel Tools"+Key.ENTER)
wait("1533806419593.png")
wait(1)
wait("1533806623650.png")
type("sadmin"+Key.TAB)
wait("1533807033983.png")
type("s3dm15q4"+Key.TAB)
type("Server"+Key.ENTER)
wait(20)
exists("1534416757603.png")
find("1534416801560.png")
click("applet.png")
wait(2)
click("1534420437010.png")
wait(1)
type(Key.F7, KeyModifier.CTRL)
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
elif exists("1534491998544.png"):
    wait("1534492064606.png")
    click("1534492092335.png")
else :
    wait("1534492161689.png")
    click("1534492179543.png")















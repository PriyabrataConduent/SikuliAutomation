import sys
import os

#login=open("accounts.txt","r")
#lines=login.readlines()
#username=lines[0].rstrip('\n')
#password=lines[1].rstrip('\n')
#server=lines[2].rstrip('\n')
#login.close()

#f=open("inputFile.txt","r")
#lines=f.readlines()
#objList=lines[0].rstrip('\n')
#f.close()

wait(2)

find("1545243629958.png")
wait("1545243629958.png")
if exists("1545243832619.png"):
    
    wait(1)
else:
    click("1538337667266.png")
find("1545243931419.png")
wait(1)
#click("Applet-1.png")
if (sys.argv[1] == "Applet"):
    click("Applet-1.png")
elif (sys.argv[1] == "Application"):
    click("Application.png")
elif (sys.argv[1] == "Screen"):
    click("Screen.png")
elif (sys.argv[1] == "Business Component"):
    click("BusinessComp.png")
elif (sys.argv[1] == "Business Object"):
    click("QBusinessUbi.png")
elif (sys.argv[1] == "Business Service"):
    click("BusinessService.png")
elif (sys.argv[1] == "Class"):
    click("Class.png")
elif (sys.argv[1] == "Command"):
    click("Command.png")
elif (sys.argv[1] == "DLL"):
    click("DLL.png")
elif (sys.argv[1] == "EIM Interface Table"):
    click("EIMInterfaceTable.png")
elif (sys.argv[1] == "Entity Relationship Diagram"):
    click("EntityRelationshipDiagram.png")
elif (sys.argv[1] == "Link"):
    click("Link.png")
elif (sys.argv[1] == "Pick List"):
    click("PickList.png")
elif (sys.argv[1] == "Project"):
    click("Proiect.png")
elif (sys.argv[1] == "Repository"):
    click("Repository.png")
elif (sys.argv[1] == "Symbolic String"):
    click("SymbolicString.png")
elif (sys.argv[1] == "Table"):
    click("Table.png")
elif (sys.argv[1] == "Task"):
    click("Task.png")
elif (sys.argv[1] == "Toolbar"):
    click("Toolbar.png")
elif (sys.argv[1] == "View"):
    click("View.png")
elif (sys.argv[1] == "Web Page"):
    click("WebPage.png")
elif (sys.argv[1] == "Web Template"):
    click("WebTemplate.png")
elif (sys.argv[1] == "Workflow Process"):
    click("WorkflowProcess.png")

else:
    exit(1)

wait(5)
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
#type(Key.F7, KeyModifier.CTRL)
exists("rightClick.png")
click("compile_selected_rightClick.png")

find("1534453184581.png")
#if exists("1534453184581.png"):
#    wait(2)
#    find("Siebelteposi.png")
#elif exists("ObjectCompil-1.png"):
    #click("Siebelreposi.png")
 #   wait(2)
 #   find("iebeteposito-1.png")
    
    #find("iebeteposito.png")
    #find("1534453234967.png")
wait(2)
#wait("1534453234967.png")
find("DbieclCompil.png")
wait("Siebelteposi-1.png")
click("Browse.png")

#click("1534453268029.png")
wait(5)
type("D:\Full_Compile\siebel_sia_09_16_2018.srf")
click("1534454073561.png")
wait("1534454164894.png")
exists("1534453184581.png")

wait(2)
click("1534454247270.png")
print("Compilation Process Started")
wait(20)
if exists("1534490859009.png"):
    wait("1534490884832.png")
    find("1534490902768.png")
    click("1534490939481.png")
    wait(2)
    wait("1534492161689.png")
    
#    click("1534492179543.png")
elif exists("1534491998544.png"):
    wait("1534492064606.png")
    click("1534492092335.png")
    print("Compilation Process Stopped due to error")
else :
    wait(1)
#    wait("1534492161689.png")
#    click("1534492179543.png")
print("Compilation Process Completed")
click("7SiebelUbiec.png")

if exists("1538906419102.png"):
    wait("1534416757603.png")
    wait(1)
    exit
else:
    click("1538337667266.png")

#click("1538906419102.png")
print("Done")
exit
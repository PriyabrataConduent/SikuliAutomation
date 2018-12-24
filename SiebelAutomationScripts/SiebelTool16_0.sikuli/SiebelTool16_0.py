import sys
import os

f=open("inputFile.txt","r")
lines=f.readlines()
objList=lines[0].rstrip('\n')
f.close()

find( "1545373968338.png" )
#wait( "1545243629958.png" )
#waitVanish("siebel_icon_red.png")
hover( "siebel_icon_red.png" )

if exists("1545243832619.png"):
    
    wait(1)
else:
    #click("1545374005703.png")
    click( "siebel_icon_red.png" )
wait("siebel_icon_red.png")
find("1545243931419.png")
find("1545629350116.png")
click("1545629367576.png")

wait(2)
find("1545289173476.png")
wait(2)
exists("1545289203954.png")
if( sys.argv[1] == "Applet" ):
    click("1545378153399.png")
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
else :
    exit
wait(3)
type('q', Key.CTRL)
wait("1545289448622.png")
paste(objList)
type(Key.ENTER)
wait(1)
#exists("1545289684427.png")
exists("1545395710614.png")
keyDown(Key.SHIFT)
click("1545395659116.png")
type(Key.ENTER)
wait("1545395837548.png")
rightClick("1545541378161.png")
exists("rightClickDialog.png")
click("CompileSelected.png")
#click("1545542219627.png")
#wait("Tools_select_options.png")
#click("Tools_Compile_Selected.png")
#type(Key.F7, KeyModifier.CTRL)
wait(1)
exists("1545291971600.png")

wait("1545292030135.png") 
#exists("1545292118361.png")
wait(1)
exists("1545293089172.png")
click("1545293064703.png")

wait(1)
exists("1545292307807.png")
paste("D:\CM\Testing\siebel_sia.srf")
wait(1)
exists("1545374122061.png")


click("1545374100598.png")
wait(2)
click("1545293373821.png")
wait(5)
print("Done")

exit
try:   
    wait("MENU.png",50)
    print "Wait Siebel Tool"
    if (sys.argv[1] == "Applet"):
         click("Applet-tree-item.png")
    elif (sys.argv[1] == "Application"):
         click("1508933627193.png")       
    elif (sys.argv[1] == "Business_Service"):
         click("Business service-tree-item.png")
    elif (sys.argv[1] == "View"):
         click("view-tree-item.png")
    elif (sys.argv[1] == "Business_Component"):
        click("BC.png") 
    elif (sys.argv[1] == "Business_Object"):
        click("BO.png")   
    elif (sys.argv[1] == "EIM_Interface_Table"):
        click("eim-t-tree-item.png")   
    elif (sys.argv[1] == "Integration_Object"):
        click("IO.png") 
    elif (sys.argv[1] == "Link"):
        click("link-tree-item.png") 
    elif (sys.argv[1] == "Pick_List"):
        click("PICKLIST.png") 
    elif (sys.argv[1] == "Screen"):
        click("screen-tree-item.png")    
    elif (sys.argv[1] == "Web_Template"):
        click("wt-tree-item.png")
    elif (sys.argv[1] == "Workflow_Process"):
       click("wf-tree-item.png")
    elif (sys.argv[1] == "Web_Page"):
      click("1508928663872.png") 
    elif (sys.argv[1] == "Symbolic_String"):
      click("1508928687048.png")
    elif (sys.argv[1] == "Table"):
      click("1508928675719.png")
    else:
         exit(1)
    type ( "q",KeyModifier.CTRL)
    wait("Name-text-input.png",200)
    click("Name-text-input.png")
    paste( sys.argv[2])
    type ( Key.ENTER)
    
    try:
        wait("Arrow-tree-element.png",200)
    except FindFailed:
        click("Siebel Objects-tree-item.png")
        print "Object not found in repository"
        exit(1)
    type ( Key.F7, KeyModifier.CTRL)
    
    print "LOG: Wait compiler window"
    wait("Object Compile_Selected Objectsr-pane-header.png",200)
    
    click("BROWSE.png")
    wait("save-and-cancel-button.png.png",50)
    paste(sys.argv[3])
    click("save_button.png.png")
    print "LOG: Set path of SRF file"
    waitVanish("save-as.png.png",200)   
    click("Compile-button.png")
    waitVanish("Object Compiler-pane-header.png",300)
    click("Siebel Objects-tree-item.png")
except FindFailed:
    click("Siebel Objects-tree-item.png")
    print "ERROR: Something wrong with Sandbox Screen. Image find failed"
    exit(1)




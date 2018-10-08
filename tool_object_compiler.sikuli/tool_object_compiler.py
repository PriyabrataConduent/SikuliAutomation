
wait("SSiebelTools.png")

click("Applet-tree-item.png")
type ( "q",KeyModifier.CTRL)
wait("Name-text-input.png",200)
click("Name-text-input.png")
paste( "Contact Quota Period List Applet")
type ( Key.ENTER)
wait("Arrow-tree-element.png",200)
    
type ( Key.F7, KeyModifier.CTRL)
    
print "LOG: Wait compiler window"
wait("Object Compile_Selected Objectsr-pane-header.png",200)
    
click("BROWSE.png")
  
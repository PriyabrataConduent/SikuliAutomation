@ECHO OFF
D:
cd D:\Automation_Siebel_Project\SiebelAutomationScripts\
ECHO Now Compilation will Start for "%1"
call runsikulix.cmd -r SiebelTool16_0.sikuli --args %1
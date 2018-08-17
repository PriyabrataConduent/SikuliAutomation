@ECHO OFF
NET SEND %ComputerName% This is line 1 of the popup message.
cd C:\Users\50000339\Documents\SikuliProjects
ECHO I am on Sikuli Folder
runsikulix.cmd -r SiebelSikuliAutomation.sikuli > SiebelSikuliAutomation.log
exit /B
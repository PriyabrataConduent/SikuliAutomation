@ECHO OFF
cls
SET FILE="D:\Automation_Siebel_Project\deploy\*.xls"
Set Counter=0
set cnt=0

D:
CD D:\Automation_Siebel_Project\SiebelAutomationScripts\
C:\Users\30096862\AppData\Local\Programs\Python\Python37\python D:\Automation_Siebel_Project\SiebelAutomationScripts\textToExcel.py

for %%A in (%FILE%) do set /a cnt+=1
echo File count = %cnt%

:start
if %Counter% == %cnt% ( goto end )
for /f "delims=" %%a in ('newest_file.py') do set "arg1=%%~na"
ECHO "%arg1%"

CD D:\Automation_Siebel_Project\SiebelAutomationScripts\
ECHO Formating User Input
C:\Users\30096862\AppData\Local\Programs\Python\Python37\python D:\Automation_Siebel_Project\SiebelAutomationScripts\formatUserXlsFile.py > D:\Automation_Siebel_Project\SiebelAutomationScripts\inputFile.txt

ECHO Now Compilation will Start for "%arg1%"
call D:\Automation_Siebel_Project\SiebelAutomationScripts\runsikulix.cmd -r D:\Automation_Siebel_Project\SiebelAutomationScripts\SiebelTool16_0.sikuli --args "%arg1%"

Set /A Counter+=1
echo %Counter%
echo "Removing latest files"
C:\Users\30096862\AppData\Local\Programs\Python\Python37\python D:\Automation_Siebel_Project\SiebelAutomationScripts\removeLatest.py
goto start
:end
echo "Done Compilation"
echo "Stopping services on Remote"
::SC \\10.36.20.41 Stop siebsrvr_NJRBTST_ET_siebsrvr1

echo "Starting GenB Script"
::D:\CM\genbscript.bat
SLEEP 5
echo "Copying srf and genb to Remote"
::robocopy D:\CM\srf1545029316_444\ \\10.36.20.41\D$\CM\Testing\srf1545029316_444  /E
::ren \\10.36.20.41\d$\Testing\siebel_sia.srf siebel_sia.srf_20181219
::copy D:\CM\siebel_sia.srf \\10.36.20.41\d$\CM\Testing\

::::ren \\10.36.20.41\d$\Siebel\15.0.0.0.0\ses\siebsrvr\OBJECTS\enu\siebel_sia.srf siebel_sia.srf_20181219

::::copy D:\CM\siebel_sia.srf \\10.36.20.41\d$\Siebel_15\15.0.0.0\ses\siebsrvr\OBJECTS\enu\siebel_sia.srf

::SC \\10.36.20.41 Start siebsrvr_NJRBTST_ET_siebsrvr1


EXIT /B
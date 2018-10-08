@ECHO OFF
:SET arg1=%1
SET FILE="D:\IncrementalCompile\deploy\*.xlsx"
:setlocal enableextensions
set file_count=0
for %%x in ("%FILE%") do set /a file_count+=1
:endlocal
ECHO %file_count%
SET cmd="for /F %%i in ("%FILE%") do @echo %%~ni"
FOR /F "tokens=*" %%a in ('%cmd%') do SET arg1=%%a
ECHO "%arg1%"
:C:\Users\50000339\Documents\SikuliProjects
CD C:\Users\50000339\Documents\SikuliProjects
ECHO Formating User Input
python formatUserXlsFile.py > inputFile.txt
ECHO Searching Siebel Tools
ECHO Now Compilation will Start for "%arg1%"
:runsikulix.cmd -r CompileSelectedSiebel.sikuli --args "%arg1%"


:SET cmd="for /F %%i in ("%FILE%") do @echo %%~ni"
:FOR /F "tokens=*" %%a in ('%cmd%') do SET arg1=%%a
:ECHO "%arg1%"
:CD C:\Users\50000339\Documents\SikuliProjects
:ECHO Formating User Input
:python formatUserXlsFile.py > inputFile.txt
:ECHO Searching Siebel Tools
:ECHO Now Compilation will Start for "%arg1%"
pause
:runsikulix.cmd -r CompileSelectedSiebel.sikuli --args "%arg1%"

:exit /B
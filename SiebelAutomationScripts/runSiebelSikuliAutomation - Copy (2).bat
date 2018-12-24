@ECHO OFF
cls
SET FILE="D:\IncrementalCompile\deploy\*.xlsx"
Set Counter=0
set cnt=0
for %%A in (%FILE%) do set /a cnt+=1
echo File count = %cnt%

:start
if %Counter% == %cnt% ( goto end )
for /f "delims=" %%a in ('newest_file.py') do set "arg1=%%~na"
ECHO "%arg1%"

CD C:\Users\50000339\Documents\SikuliProjects\
ECHO Formating User Input
python formatUserXlsFile.py > inputFile.txt

ECHO Now Compilation will Start for "%arg1%"
call C:\Users\50000339\Documents\SikuliProjects\runsikulix.cmd -r C:\Users\50000339\Documents\SikuliProjects\CompileSelectedSiebel.sikuli --args "%arg1%"

Set /A Counter+=1
echo %Counter%
echo "Removing latest files"
python C:\Users\50000339\Documents\SikuliProjects\removeLatest.py
goto start
:end
echo "Done"
EXIT /B
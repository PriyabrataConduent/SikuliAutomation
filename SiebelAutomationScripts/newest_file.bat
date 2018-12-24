@ECHO OFF
::SET FILE="D:\IncrementalCompile\deploy\*.xlsx"
::SET cmd="for /F %%i in ("%FILE%") do @echo %%~ni"
::FOR /F "tokens=*" %%a in ('%cmd%') do SET arg1=%%a
::ECHO "%arg1%"

::for /f "delims=" %%a in ('removeLatest.py') do set "var=%%a"

for /f "delims=" %%a in ('removeLatest.py') do set "var=%%~na"
ECHO "%var%"
:SET cmd="for /F %%i in ("%var%") do @echo %%~ni" 
:FOR /F "tokens=*" %%b in ('%cmd%') do SET arg1=%%b 
:ECHO "%arg1%" 



PAUSE
@ECHO OFF
:CD /d D:\Siebel\8.1.1.16.0\Tools\BIN\
ECHO Starting Siebel Tools
:siebdev.exe /c D:\Siebel\8.1.1.16.0\Tools\BIN\enu\tools.cfg /d ServerDataSrc /u SADMIN /p s3dm15q4
start D:\Siebel\15.0.0.0.0\Tools\bin\siebdev.exe /c D:\Siebel\15.0.0.0.0\Tools\BIN\enu\tools.cfg /d ServerDataSrc /u SADMIN /p sadminoui
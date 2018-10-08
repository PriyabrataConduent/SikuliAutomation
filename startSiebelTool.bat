@ECHO OFF
:CD /d D:\Siebel\8.1.1.16.0\Tools\BIN\
ECHO Starting Siebel Tools
:siebdev.exe /c D:\Siebel\8.1.1.16.0\Tools\BIN\enu\tools.cfg /d ServerDataSrc /u SADMIN /p s3dm15q4
start D:\Siebel\8.1.1.16.0\Tools\BIN\siebdev.exe /c D:\Siebel\8.1.1.16.0\Tools\BIN\enu\tools.cfg /d ServerDataSrc /u SADMIN /p s3dm15q4
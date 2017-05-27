cls
@echo off

setlocal
set PATH=%PATH%;C:\mingw\bin;C:\mingw\msys\1.0\bin

echo *************************************************
echo This script compile you Windows  project
echo *************************************************
echo PREREQUISITE:
echo Have MinGW installed on your computer

pause

call make

echo Now your driver is ready

pause
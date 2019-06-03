@echo off
set basedir=%~dp0..\..\..\
set version_rev=git rev-parse --short HEAD
echo %version_rev%
: git rev-parse --short HEAD

: fbs run

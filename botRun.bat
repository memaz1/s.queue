@ECHO off && set "rootFolder=%~dp0" && SETLOCAL ENABLEDELAYEDEXPANSION & if exist "%~dp0.cache\key1.txt" cd "%~dp0.cache" && for /F "skip=1 eol=; delims=" %%i in (key1.txt) do (set "simpleKey!count!=%%i" && SET /a "count=!count!+1")
cd "%rootFolder%" && if "%simpleKey%"=="@key@" ECHO %simpleKey:~0,1% & title Developer ^mode && ping 192.0.2.2 -n 1 -w 500 > nul & cls & powershell write-host -fore CYAN Key validated. && ECHO %simpleKey:~0,1%*****%simpleKey:~4% && ping 192.0.2.2 -n 1 -w 2350 > nul
if not exist "%~dp0.cache\key1.txt" MKDIR "%~dp0.cache" & ECHO ;-- simpleKey> "%~dp0.cache\key1.txt" & cls

for /l %%h in (1, 1, 255) do cd "C:\Users\memaz\Python-Discord-Bot-Template" && python bot.py

if "%pause%"=="1" (ping 192.0.2.2 -n 1 -w 500 > nul & ECHO Waiting^.^.^. && PAUSE >nul) else (ping 192.0.2.2 -n 1 -w 500 > nul & EXIT)
%% &:: Basic batch file template         v1.2+5| Mood#6030
%% &:: simpleKey & pause split                 | https://steamcommunity.com/id/mo-od/

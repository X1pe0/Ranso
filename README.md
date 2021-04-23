# Ranso
Ransomware Canary Checker

Realtime watch of canary files on all user profiles on the NT system. Can be installed as a service via NSSM and or included in the build is a background VBS that can be added to startup via registry. A config file is also used (has to be within the same directory as the EXE). Ranso.exe built using Nuitka/GCC for Windows. 

'C:\User\Example~> ranso.exe' (Realtime check and verify files)

'C:\User\Example~> ranso.exe create' (Remove log history and re-create verification files)

Commands can also be sent when a file has been removed/crypted/touched such as 'shutdown' or 'ipconfig /release'.

## Log Location

C:\ranso.log 

## Images

![](https://nabyte.com/imgs/49bdd383b24a710b6b4d6654f0e987ee88ef7b56Capture.png)

![](https://nabyte.com/imgs/759903be5d268eb0646ef259905b855f722e4747p2.png)

## Folder Locations (All users on the Windows System.)


            f = open("%s/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            f = open("%s/Downloads/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            f = open("%s/Documents/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()        
            f = open("%s/Contacts/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            f = open("%s/AppData/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()   
            f = open("%s/Favorites/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            f = open("%s/Links/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            f = open("%s/Pictures/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            f = open("%s/Videos/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            f = open("%s/Searches/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()

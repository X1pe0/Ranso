# Ranso
Ransomware Canary Checker
(ranso.exe built using Nuitka/GCC for Windows. 

'C:\User\Example~> ranso.exe check' (Check and verify files)

'C:\User\Example~> ranso.exe create' (Remove log history and re-create verification files)

## Log Location
%TEMP%\ranso.log 

## Images

![](https://nabyte.com/imgs/49bdd383b24a710b6b4d6654f0e987ee88ef7b56Capture.png)

## Folder Locations


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

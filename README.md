# Ranso
Ransomware Canary Checker

Realtime watch of canary files on all user profiles on the NT system. Can be installed as a service via NSSM and or included in the build is a background VBS that can be added to startup via registry. A config file is also used (has to be within the same directory as the EXE). Ranso.exe built using Nuitka/GCC for Windows. 

'C:\User\Example~> ranso.exe' (Realtime check and verify files)

'C:\User\Example~> ranso.exe create' (Remove log history and re-create verification files)

Commands can also be sent when a file has been removed/crypted/touched such as 'shutdown' or 'ipconfig /release'.

One click installer: https://github.com/X1pe0/Ranso/raw/master/Ranso.Builds/Ranso.OInstall.exe (Follow the default install path to run as portable background "agent")

"Plugins" can also be used by adding a standard PY file within the 'ransoplugins' folder. (Not needed and will run w/o plugins)

## Config File
```
Line 1: ranso.txt                                                #Name of canary file.
Line 2: ranso.log                                                #Name of log file.
Line 3: This is a ransomware test file. Please ignore.           #Text within canary file.
Line 4:                                                          #Debug Mode. (True/False)
Line 5: echo "Detected!"                                         #Command to be ran when detected.
Line 6:                                                          #Canary files hidden? (True/False)
Line 7: 1                                                        #How many X Seconds to check files.
```
## Log Location

C:\ranso.log 

## Images

![](https://nabyte.com/imgs/49bdd383b24a710b6b4d6654f0e987ee88ef7b56Capture.png)

![](https://nabyte.com/imgs/759903be5d268eb0646ef259905b855f722e4747p2.png)

![](https://nabyte.com/imgs/76e58323f5d73a4f587af5921fe73f4f83c6a200p3.png)

## Folder Locations (All users on the Windows System.)

Python: 

```
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
```

Plain: 

```
(All Users) -> User Root Dir
(All Users) -> Downloads
(All Users) -> Documents
(All Users) -> Contacts
(All Users) -> AppData
(All Users) -> Favorites
(All Users) -> Links
(All Users) -> Pictures
(All Users) -> Videos
(All Users) -> Searches
```

## Issues downloading (Due to AV or firewall)? 

Save this image and rename to install.zip

![](https://nabyte.com/imgs/caab55160300965b96a9304a26adab6a7ba835acinstaller.png)

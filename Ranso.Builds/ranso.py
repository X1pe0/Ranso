import os
import sys
import time
import ctypes
import subprocess
from glob import glob
from datetime import datetime
#############Globals##############

filename = 'ranso.txt'                                                 #Canary file name.
logit = 'ranso.log'                                                    #Log file name (C:\ranso.log).
txt = 'This is a ransomware test file. Please ignore.'                 #Content of canary file.
usrs = glob("C:/Users/*")                                              #Gather all user folders.
debug = False                                                          #Debug mode (Shows output).
com_when_detect = ''                                                   #Command to run when detected.
hidden = True                                                          #Want file to be hidden from users?
scanrate = 1                                                           #Scan canary files every X seconds.

##################################
try:
 is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == False:
        print ("Please run as admin.")
        exit(0)
if os.name =="nt":
    pass
else:
    print ('This tool is for a windows system.')
    exit(0)
def logo():
    print('''
 ____                                       
/\  _`\                                     
\ \ \L\ \     __      ___     ____    ___   
 \ \ ,  /   /'__`\  /' _ `\  /',__\  / __`\ 
  \ \ \\\\ \ /\ \L\.\_/\ \/\ \/\__, `\/\ \L\ \\
   \ \_\ \_\ \__/.\_\ \_\ \_\/\____/\ \____/
    \/_/\/ /\/__/\/_/\/_/\/_/\/___/  \/___/ 
            Ransomware Canary Check \n''')
def h():
    logo()
    print ('Args: create')
    print ('ranso.py <arg>')
try:
    var = str(sys.argv[1])
except:
    var = ''
def main():
    today = str(datetime.now())
    if var == 'create':
        try:
            f = open("C:/%s"%(logit), "w")
            f.write('')
            f.close()
        except:
            print ('WARNING: Unable to clear log file...')
        try:
            f = open("%s/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/%s"%(usr,filename)])
            f = open("%s/Downloads/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Downloads/%s"%(usr,filename)])
            f = open("%s/Documents/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Documents/%s"%(usr,filename)])        
            f = open("%s/Contacts/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Contacts/%s"%(usr,filename)])
            f = open("%s/AppData/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/AppData/%s"%(usr,filename)])   
            f = open("%s/Favorites/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Favorites/%s"%(usr,filename)])
            f = open("%s/Links/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Links/%s"%(usr,filename)])
            f = open("%s/Pictures/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Pictures/%s"%(usr,filename)])
            f = open("%s/Videos/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Videos/%s"%(usr,filename)])
            f = open("%s/Searches/%s"%(usr,filename), "w")
            f.write(txt)
            f.close()
            if hidden == True:
                subprocess.check_call(["attrib","+H","%s/Searches/%s"%(usr,filename)])
            exit(0)
        except:
            if debug == True:
                print ('Unable to create test files. Invalid permissions or disk space full.')  
            exit(0)   
    else:
        try:
            f = open("C:/%s"%(logit), "w")
            f.write('')
            f.close()
        except:
            print ('WARNING: Unable to clear log file...')
        try:
            checkit = open("%s/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/%s is valid."%(usr,filename))
                pass
                
            else:
                if debug == True:
                    print(today + " %s/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today + " %s/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
                    
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
           
        try:
            checkit = open("%s/Downloads/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Downloads/%s is valid."%(usr,filename))
                pass
 
            else:
                if debug == True:
                    print("%s/Downloads/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Downloads/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
                    
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Downloads/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Downloads/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
                
        try:
            checkit = open("%s/Documents/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Documents/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/Documents/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Documents/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Documents/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Documents/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
        try:
            checkit = open("%s/Contacts/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Contacts/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/Contacts/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Contacts/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Contacts/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Contacts/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
        try:
            checkit = open("%s/AppData/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/AppData/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/AppData/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/AppData/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/AppData/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/AppData/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
        try:
            checkit = open("%s/Favorites/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Favorites/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/Favorites/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Favorites/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Favorites/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Favorites/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
        try:
            checkit = open("%s/Links/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Links/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/Links/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Links/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Links/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Links/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
        try:
            checkit = open("%s/Pictures/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Pictures/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/Pictures/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Pictures/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Pictures/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Pictures/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
        try:
            checkit = open("%s/Videos/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Videos/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/Videos/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Videos/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Videos/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Videos/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
        try:
            checkit = open("%s/Searches/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                if debug == True:
                    print("%s/Searches/%s is valid."%(usr,filename))
                pass
            else:
                if debug == True:
                    print("%s/Searches/%s has been changed!\n"%(usr,filename))
                try:
                    f = open("C:/%s"%(logit), "a")
                    f.write(today+" %s/Searches/%s has been changed!\n"%(usr,filename))
                    f.close()
                    if com_when_detect == '':
                        pass
                    else:
                        os.system(com_when_detect)
                except:
                    if debug == True:
                        print ('WARNING: Unable to update log.')
                    pass
        except:
            if debug == True:
                print ('\n' + today + ' Unable to check file %s/Searches/%s'%(usr,filename))
            try:
                f = open("C:/%s"%(logit), "a")
                f.write('\n' + today + ' Unable to check file %s/Searches/%s'%(usr,filename))
                f.close()
            except:
                if debug == True:
                    print ('WARNING: Unable to update log.')
                pass
while True:
    for usr in usrs:
        if usr == 'C:/Users\\desktop.ini':
            pass
        elif usr == 'C:/Users\\All Users':
            pass
        elif usr == 'C:/Users\Default User':
            pass
        elif usr == 'C:/Users\Default':
            pass
        elif usr == 'C:/Users\Public':
            pass
        else:
            time.sleep(scanrate)
            main()

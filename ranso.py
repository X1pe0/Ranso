import os
import sys
import time
import ctypes
from glob import glob
#############Globals##############

filename = 'ranso.txt'
logit = 'ranso.log'
txt = 'This is a ransomware test file. Please ignore.'
usrs = glob("C:/Users/*")

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
    print ('Args: check, create')
    print ('ranso.py <arg>')
try:
    var = str(sys.argv[1])
except:
    h()
    exit(0)
def main():
    print ('\n')
    if var == 'create':
        try:
            f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
            f.write('')
            f.close()
        except:
            print ('WARNING: Unable to clear log file...')
        try:
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
        except:
            print ('Unable to create test files. Invalid permissions or disk space full.')     
    elif var == 'check':
        try:
            f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
            f.write('')
            f.close()
        except:
            print ('WARNING: Unable to clear log file...')
        try:
            checkit = open("%s/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/%s is valid."%(usr,filename))
            else:
                print("%s/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Downloads/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Downloads/%s is valid."%(usr,filename))
            else:
                print("%s/Downloads/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Downloads/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Downloads/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Downloads/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Documents/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Documents/%s is valid."%(usr,filename))
            else:
                print("%s/Documents/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Documents/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Documents/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Documents/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Contacts/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Contacts/%s is valid."%(usr,filename))
            else:
                print("%s/Contacts/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Contacts/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Contacts/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Contacts/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/AppData/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/AppData/%s is valid."%(usr,filename))
            else:
                print("%s/AppData/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/AppData/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/AppData/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/AppData/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Favorites/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Favorites/%s is valid."%(usr,filename))
            else:
                print("%s/Favorites/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Favorites/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Favorites/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Favorites/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Links/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Links/%s is valid."%(usr,filename))
            else:
                print("%s/Links/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Links/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Links/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Links/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Pictures/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Pictures/%s is valid."%(usr,filename))
            else:
                print("%s/Pictures/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Pictures/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Pictures/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Pictures/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Videos/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Videos/%s is valid."%(usr,filename))
            else:
                print("%s/Videos/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Videos/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Videos/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Videos/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
        try:
            checkit = open("%s/Searches/%s"%(usr,filename))
            line = checkit.read().replace("\n", " ")
            checkit.close()
            if line == txt:
                print("%s/Searches/%s is valid."%(usr,filename))
            else:
                print("%s/Searches/%s has been changed!"%(usr,filename))
                try:
                    f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                    f.write("%s/Searches/%s has been changed!"%(usr,filename))
                    f.close()
                except:
                    print ('WARNING: Unable to update log.')
        except:
            print ('Unable to check file %s/Searches/%s'%(usr,filename))
            try:
                f = open("%s/AppData/Local/Temp/%s"%(usr,logit), "w")
                f.write('Unable to check file %s/Searches/%s'%(usr,filename))
                f.close()
            except:
                print ('WARNING: Unable to update log.')
    else:
        h()
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
        main()

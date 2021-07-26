import PyInstaller.__main__
import shutil
import os


filename="malicious.py"
exename="benign.exe"
icon="Firefox.ico"
pwd=os.getcwd()

if os.path.isfile(exename):
    os.remove(exename)

PyInstaller.__main__.run([
    "malicious.py",
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename,
    "--icon="+icon
])

print("EXE Created")

#Clean up after PyInstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")
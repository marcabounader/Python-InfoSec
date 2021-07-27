import pathlib

def getTimeStamps(filename):
    fname=pathlib.Path(filename)
    stats=fname.stat()
    if not fname.exists():
        return []
    return(stats.st_ctime,stats.st_mtime,stats.st_atime)

def checkTimeStamps(filename,create,modify,access):
    stats=getTimeStamps(filename)
    if len(stats)==0:
        return False
    (ctime,mtime,atime)=stats
    if float(create) != float(ctime):
        return False
    elif float(modify) != float(mtime):
        return False
    elif float(access) != float(atime):
        return False
    return True

def checkDecoyFiles():
    with open("decoys.txt","r") as f:
        for line in f:
            vals=line.rstrip().split(",")
            if not checkTimeStamps(vals[0],vals[1],vals[2],vals[3]):
                print("%s has been tempered with."% vals[0])

checkDecoyFiles()
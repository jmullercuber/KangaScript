import os

# need these to interpret and import another KangaScript
#from ksparser import parser as ksparser
#from ksinterpreter import interpret as ksinterpret
#from ksinterpreter import GlobalEnv

def importFile(path, pwd):
    fileLoc = pwd + "/" + "/".join(path) + ".ks"
    print("Importing single file", fileLoc)
    if os.path.isfile(fileLoc):
        # if file exists
        # evaluate it
        # TODO: actually eval, use different pwd for global env
        return GlobalEnv("~")


def importDir(path, pwd):
    dirLoc = pwd + "/" + "/".join(path[:-1]+[]) + "/"
    if os.path.isdir(dirLoc):
        # if dir exists
        pass
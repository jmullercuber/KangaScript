import os

# need these to interpret and import another KangaScript
#from ksparser import parser as ksparser
#from ksinterpreter import interpret as ksinterpret
#from ksinterpreter import GlobalEnv

def importFile(path, pwd):
    # find the KS source
    fileLoc = pwd + "/" + "/".join(path) + ".ks"
    print("Importing single file", fileLoc)
    if os.path.isfile(fileLoc):
        # if file exists
        # evaluate the KS code
        # TODO: actually eval
        return GlobalEnv( os.path.abspath(os.path.dirname(fileLoc)) )


def importDir(path, pwd):
    dirLoc = pwd + "/" + "/".join(path[:-1]+[]) + "/"
    if os.path.isdir(dirLoc):
        # if dir exists
        pass
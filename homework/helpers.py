import os

def read_file(path:str):
    """
    read file and return first line
    """
    if os.path.exists(path):
        with open(path,"r") as file:
            content=file.read()
            return content
    else:
        return None

def filenames(folder:str):
    fname=folder.split("/")[-1]
    flist=[]
    for f in os.listdir(folder):
        flist.append(folder+"/"+f)
    return flist

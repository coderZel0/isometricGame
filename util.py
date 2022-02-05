from csv import reader
from math import sqrt

def fileData(file):
    mList =[]
    with open(file,'r') as f:
        data = reader(f,delimiter=',')
        for d in data:
            mList.append(d)
    return mList    

def getFrames(path)->list:
    pass

def calDist(pos1,pos2):
    return sqrt(abs((pos2[0]-pos1[0])**2-(pos2[1]-pos1[1])**2))
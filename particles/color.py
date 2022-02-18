class Color:
    def __init__(self,value:tuple,name:str="white"):
        self.__inColor = value
        self.colName = name
        self.color = self.__getColor(self.__inColor)

    def __colorMap(self,color:float)->int:
        if color>1: color =1
        if color<0: color =0
        mapToStart = 0
        mapToEnd = 255
        mapFromStart =1
        mapFromEnd =0
        return int(((color-mapFromStart)/(mapFromEnd-mapFromStart))*(mapToStart-mapToEnd)+mapToEnd)

    def __getColor(self,color:tuple)->tuple:
        return tuple(map(self.__colorMap,color))

    def __add__(self,other):
        return Color(tuple(col[0]+col[1] for col in zip(self.__inColor,other.__inColor)))

    def __mul__(self,other):
        return Color(tuple(col[0]*col[1] for col in zip(self.__inColor,other.__inColor)))    
   
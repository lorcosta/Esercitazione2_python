import math
class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,secondoPunto):
        return math.sqrt((self.x-secondoPunto.x)**2+(self.y-secondoPunto.y)**2)
    def move(self,nuovaX,nuovaY):
        self.x+=nuovaX
        self.y+=nuovaY
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

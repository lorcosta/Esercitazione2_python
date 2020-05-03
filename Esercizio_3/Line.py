import math
from Point import *
class Line:
    def __init__(self,m,q):
        self.m=m
        self.q=q
    def __str__(self):
        return "y="+str(self.m)+"x+"+str(self.q)
    def line_from_points(self,puntoA,puntoB):
        m=(puntoB.y-puntoA.y)/(puntoB.x-puntoA.x)
        q=((puntoB.y-puntoA.y)/(puntoB.x-puntoA.x)*(puntoA.x))+puntoA.y
        l=Line(m,q)
        return "y="+str(self.m)+"x+"+str(self.q)
    def distance(self,punto):
        dist=abs(punto.y-((self.m*punto.x)+self.q))/(math.sqrt(1+self.m**2))
        return dist
    def intersection(self,linea):
        puntoX=(linea.q-self.q)/(self.m-linea.m)
        puntoY=(self.m*((linea.q-self.q)/(self.m-linea.m)))+self.q
        point=Point(puntoX,puntoY)
        return point

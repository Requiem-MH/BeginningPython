# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 17:57:10 2018

@author: Michael Harrop
"""
from math import pi
from math import sqrt

class Circle2D(object):
    def __init__(self, x = 0, y = 0, radius = 1):
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__center = (x, y)
        
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def setRadius(self, radius):
        self.__radius = radius
        
    def setCenter(self, x, y):
        self.__center = (x, y)
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getRadius(self):
        return self.__radius
    
    def getCenter(self):
        return self.__center
    
    def getArea(self):
        return pi * self.__radius ** 2
    
    def getPerimeter(self):
        return 2 * pi * self.__radius
    
    def containsPoints(self, x, y):
        if x <= self.__radius and y <= self.__radius:
            return True
        else:
            return False
        
    def contains(self, circle2D):
        distance = round(sqrt((circle2D.getX()-self.getX())**2 + (circle2D.getY() - self.getY())**2))
        distance2 = distance + circle2D.getRadius()
        
        if self.getRadius() > distance2:
            return True
        else:
            return False
        
    def overlaps(self, circle2D):
        distance = round(sqrt((circle2D.getX()-self.getX())**2 + (circle2D.getY() - self.getY())**2))
        distance2 = circle2D.getRadius() + self.getRadius() 
        if distance2 >= distance and self.contains(circle2D) != True:
            return True
        else:
            return False
        
    def __contains__(self, another):
        distance = round(sqrt((another.getX()-self.getX())**2 + (another.getY() - self.getY())**2))
        distance2 = distance + self.getRadius()
        if another.getRadius() > distance2:
            return True
        else:
            return False
    def __cmp__(self, circle):
        circle1 = self.getRadius()
        circle2 = circle.getRadius()
        if circle1 < circle2:
            return self.__lt__(circle)
        elif circle1 <= circle2:
            return self.__le__(circle)
        elif circle1 > circle2:
            return self.__gt__(circle)
        elif circle1 >= circle2:
            return self.__ge__(circle)
        elif circle1 == circle2:
            return self.__eq__(circle)
        elif circle1 != circle2:
            return self.__ne__(circle)
              
    def __lt__(self, circle):
        if self.getRadius() < circle.getRadius():
            return True
        else:
            return False
    
    def __le__(self, circle):
        if self.getRadius() <= circle.getRadius():
            return True
        else:
            return False

    def __gt__(self, circle):
        if self.getRadius() > circle.getRadius():
            return True
        else:
            return False
        
    def __ge__(self, circle):
        if self.getRadius() >= circle.getRadius():
            return True
        else:
            return False
        
    def __eq__(self, circle):
        if self.getRadius() == circle.getRadius():
            return True
        else:
            return False
        
    def __ne__(self, circle):
        if self.getRadius() != circle.getRadius():
            return True
        else:
            return False
        
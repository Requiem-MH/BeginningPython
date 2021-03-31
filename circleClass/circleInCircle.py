# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 16:52:52 2018

@author: Michael Harrop
"""
from circleClass import Circle2D

x1, y1, radius1 = eval(input("Enter x1, y1, and radius1: "))
x2, y2, radius2 = eval(input("Enter x2, y2, and radius2: "))

c1 = Circle2D(x1, y1, radius1)
c2 = Circle2D(x2, y2, radius2)

print("\nArea for c1 is", c1.getArea())
print("Perimeter for c1 is", c1.getPerimeter())
print("\nArea for c1 is", c2.getArea())
print("Perimeter for c1 is", c2.getPerimeter())
print("\nc1 contains the center of c2?", c1.containsPoints(c2.getX(), c2.getY()))
print("c1 contains c2?", c1.contains(c2))
print("c1 overlaps c2?", c1.overlaps(c2))



# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:35:17 2018

@author: Michael Harrop
"""
from tkinter import *

class EtchASketch:
    def __init__(self):
        window = Tk()
        window.title("Etch-a-Sketch")
        self.canvas = Canvas(window, width=800, height=600, bg="white")
        self.canvas.pack()
        #self.canvas.create_line(0, 0, 799, 599, fill="black", tags="line")
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()
        self.START_X = 399
        self.START_Y = 299
        self.DELTA = 5
        self.current_x = self.START_X
        self.current_y = self.START_Y
        self.loc_stack = []
        self.loc_stack.append([self.current_x, self.current_y])
        self.count = 0
        window.mainloop()

    def processKeyEvent(self,event):
        #print("keysym? ", event.keysym)
        #print("char? ", event.char)
        #print("keycode? ", event.keycode)
        if event.keysym in ("Up","Down","Left","Right"):
            if event.keysym == "Up":
                dx, dy = 0, -self.DELTA
            elif event.keysym == "Down":
                dx, dy = 0, self.DELTA
            elif event.keysym == "Left":
                dx, dy = -self.DELTA, 0
            elif event.keysym == "Right":
                dx, dy = self.DELTA,0
            new_x = self.current_x + dx
            new_y = self.current_y + dy
            self.count = self.count + 1
            tag = "line" + str(self.count)
            self.canvas.create_line(self.current_x, self.current_y, new_x, new_y, fill="black", tags=tag)
            self.current_x = new_x
            self.current_y = new_y
            self.loc_stack.append([self.current_x, self.current_y])
        if event.keysym == "BackSpace":
            if self.count > 0:
                tag = "line" + str(self.count)
                self.canvas.delete(tag)
                self.loc_stack.pop()
                self.count = self.count - 1
                self.current_x, self.current_y = self.loc_stack[-1]
        
EtchASketch()
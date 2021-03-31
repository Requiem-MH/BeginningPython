from tkinter import *
import math

class Circle:
    def __init__(self):
        window = Tk()
        window.title("circle")
        self.radius = 50
        self.center = [100, 60]  # initialize to the original center of the canvas
        self.canvas = Canvas(window, width = 300, height = 120, bg = "white")
        self.canvas.pack()
        self.canvas.create_oval(50, 10, 150, 110, tags = "circle")
        self.canvas.create_text(100, 60, text = "", tags = "text")
        self.canvas.bind('<B1-Motion>', self.getWords)
        self.canvas.focus_set()

        window.mainloop()

    def getWords(self, event):
        self.canvas.delete("text")
        distance = math.sqrt(((self.center[0] - event.x) ** 2) + ((self.center[1] - event.y) ** 2))
        place = ''
        if distance <= self.radius:
            place = 'inside'
        else:
            place = 'outside'
        self.canvas.create_text(self.center[0],  self.center[1],
                                    text = "Mouse pointer is %s the circle" % place,
                                    fill = "black", tag = "text")

Circle()
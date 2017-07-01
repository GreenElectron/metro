import numpy as np
from math import *
from Tkinter import *
from matplotlib import colors

canvas_width = 400
canvas_height = 400
camera_ini_x = 0
camera_ini_y = 0
scale_ini = 1



### CLASSES
class Camera:
    def __init__(self, x = camera_ini_x, y = camera_ini_y, scale = scale_ini):
        self.x = x
        self.y = y
        self.scale = scale
        
    def set_xy(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        return None
    
    def set_scale(self, new_scale):
        self.scale = new_scale
        return None
    
    
    

class PaintIns:          # Painting Instructions
    def __init__(self, canvas, priority = 1):
        self.canvas = canvas
        self.priority = priority
        
    def paint(self, x, y):
        pass


class PaintBox(PaintIns):
    def __init__(self, canvas, width=10, height=10, colour='white'):    # color is an integer - index of the color-list
        PaintIns.__init__(self, canvas)
        self.width = width
        self.height = height
        self.colour = colour
        
    def change_colour(self, colour):
        self.canvas.itemconfig(self.paint, fill=colour)
        
    def paint(self, x, y):
        self.box = self.canvas.create_rectangle(x - .5*self.width, y - .5*self.height, x + .5*self.width, y + .5*self.height, fill=self.colour)

### GLOBAL FUNCTIONS
def paint_loop(paint_list, camera, canv):     
    #TODO : sort by priority
    canv.delete('all')
    for ((x, y), obj) in paint_list:
        obj.paint(int(x - camera.x + .5 * canvas_width), int(- y + camera.y + .5 * canvas_height))
    


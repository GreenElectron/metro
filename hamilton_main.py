from hamilton_model import *
from hamilton_gfx import *

box = Particle(['freefall'])
box.x = 10.
box.y = 0.
box.u = 0.
box.v = 0.

H = Hamilton([freefall], [])



camera = Camera()


#def palo():
#paint_loop([[[int(box.x), int(box.y)], box.pb]], camera)
#    return None
#palo()
root = Tk()
root.title('Hamilton')
canv = Canvas(root, width=canvas_width, height=canvas_height, background='black')
canv.pack()
box.pb = PaintBox(canv)
while 1:
    H.propagate([box])
    paint_list = [[[box.x,box.y], box.pb]]
    paint_loop(paint_list, camera, canv)
    root.update_idletasks()
    root.update()

#pb.paint(195, 195)
#    print box.y



root.mainloop()
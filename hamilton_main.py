from hamilton_model import *
from hamilton_gfx import *

box1 = Particle(['freefall','drawable'])
box1.x = 10.
box1.y = 0.
box1.u = 0.
box1.v = 0.
box2 = Particle(['freefall','drawable'])
box2.x = -10.
box2.y = 0
box2.u = 5
box2.v = 10


H = Hamilton([freefall], [], [drawlist])



camera = Camera()


#def palo():
#paint_loop([[[int(box.x), int(box.y)], box.pb]], camera)
#    return None
#palo()
root = Tk()
root.title('Hamilton')
canv = Canvas(root, width=canvas_width, height=canvas_height, background='black')
canv.pack()
box1.pb = PaintBox(canv)
box2.pb = box1.pb
while 1:
    H.run_free([box1, box2])
    #paint_list = [[[box1.x,box1.y], box1.pb],[[box2.x,box2.y], box2.pb]]
    paint_list = H.run1_coll([box1, box2])
    paint_loop(paint_list, camera, canv)
    root.update_idletasks()
    root.update()

#pb.paint(195, 195)
#    print box.y



root.mainloop()
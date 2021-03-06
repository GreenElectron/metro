from hamilton_model    import *
from hamilton_gfx      import *
from hamilton_platform import *

H = Hamilton([freefall, testfloor, otherfloor, testwall], [], [drawlist])

root = Tk()
root.title('Hamilton')
canv = Canvas(root, width=canvas_width, height=canvas_height, background='black')
canv.pack()
camera = Camera()

box1 = Particle(['freefall','drawable','testfloor'])
box1.x  = [10.,0.]
box1.dx = [0.,0.]
box1.pb = PaintBox(canv)

box2 = Particle(['freefall','drawable','otherfloor','testwall'])
box2.x  = [-10.,0]
box2.dx = [5.,10.]
box2.pb = box1.pb

floor = Particle(['floor','drawable'])
floor.x  = [0,-75]
floor.pb = PaintBox(canv,100)

particles = [box1, box2, floor]

while 1:
    particles = H.run_free(particles)
    paint_loop(H.run1_coll(particles), camera, canv)
    root.update_idletasks()
    root.update()

root.mainloop()
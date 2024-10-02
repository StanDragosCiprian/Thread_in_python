from UI import Ui
import time
import threading
from CreateThread import CreateT

ui = Ui()

def animate_sphere(thread, canva, oval, x, y, dx, dy):
    if thread.cond:
        x += dx
        y += dy
        canva.coords(oval, x, y, x+70, y+70)
        canva.after(20, animate_sphere, thread, canva, oval, x, y, dx, dy)

canva, oval = ui.sphere()
t=CreateT(target=animate_sphere,args=(canva, oval, 10, 10, 1, 1))
ui.make_buttons(name="Start", event=t.start)
ui.make_buttons(row=1, name="Suspent", event=t.pause)
ui.make_buttons(row=2, name="Resume", event=t.resume)


ui.main()

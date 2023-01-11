import math
from tkinter import *


def calculate_position(data):
    # unpack data
    center_x, center_y, radius, distance, angle, angle_speed, x, y, color = data

    # calculate new position of object
    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))

    # save positon so other object can use it as its center of rotation
    data[6] = x
    data[7] = y

    # calcuate oval coordinates
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2, color


def create_object(data):
    # calculate oval coordinates
    x1, y1, x2, y2, color = calculate_position(data)

    # create oval
    return c.create_oval(x1, y1, x2, y2, fill=color)


def move_object(object_id, data):
    # calculate oval coordinates
    x1, y1, x2, y2, color = calculate_position(data)

    # move oval
    c.coords(object_id, x1, y1, x2, y2)


def animate():
    mercury[4] += mercury[5]
    move_object(mercury_id, mercury)

    venus[4] += venus[5]
    move_object(venus_id, venus)

    earth[4] += earth[5]
    move_object(earth_id, earth)

    moon[0] = earth[6]
    moon[1] = earth[7]

    moon[4] += moon[5]
    move_object(moon_id, moon)

    mars[4] += mars[5]
    move_object(mars_id, mars)

    jupiter[4] += jupiter[5]
    move_object(jupiter_id, jupiter)

    saturn[4] += saturn[5]
    move_object(saturn_id, saturn)

    uranus[4] += uranus[5]
    move_object(uranus_id, uranus)

    root.after(100, animate)


WIDTH = 1000
HEIGHT = 800

center_x = WIDTH // 2
center_y = HEIGHT // 2

sun = [center_x, center_y, 50, 0, 0, 0, 0, 0, "yellow"]
mercury = [center_x, center_y, 7, 70, 0, 23.68, 0, 0, "#e5e5e5"]
venus = [center_x, center_y, 10, 110, 0, 17.51, 0, 0, "#928590"]
earth = [center_x, center_y, 15, 160, 0, 14.89, 0, 0, "blue"]
moon = [0, 0, 5, 23, 0, 0.51, 0, 0, "#bdd0e4"]
mars = [center_x, center_y, 18, 220, 0, 12.065, 0, 0, "#a1251b"]
jupiter = [center_x, center_y, 28, 285, 0, 6.535, 0, 0, "#9abeb7"]
saturn = [center_x, center_y, 26, 360, 0, 4.845, 0, 0, "#fae5bf"]
uranus = [center_x, center_y, 18, 425, 0, 3.405, 0, 0, "blue"]

root = Tk()
root.title("Solar System")

c = Canvas(root, width=WIDTH, heigh=HEIGHT, bg="black")
c.pack()

sun_id = create_object(sun)
mercury_id = create_object(mercury)
venus_id = create_object(venus)
earth_id = create_object(earth)
mars_id = create_object(mars)
jupiter_id = create_object(jupiter)
saturn_id = create_object(saturn)
uranus_id = create_object(uranus)

moon[0] = earth[6]
moon[1] = earth[7]
moon_id = create_object(moon)

animate()

root.mainloop()

import math
from tkinter import *


def calculate_position(data):
    center_x, center_y, radius, distance, angle, angle_speed, x, y = data

    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))

    data[6] = x
    data[7] = y

    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2


def create_object(data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    # create oval
    return c.create_oval(x1, y1, x2, y2)


def move_object(object_id, data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    # move oval
    c.coords(object_id, x1, y1, x2, y2)


def animate():
    move_oval[4] += move_oval[5]
    move_object(e_id, move_oval)

    root.after(101, animate)


def get_direction():
    return int(input("Направление движения: \n1) По часовой\n2) Против часовой\n"))


def init():
    global move_oval
    direction = get_direction()
    center_oval = [center_x, center_y, 200, 0, 0, 0, 0, 0]
    if direction == 1:
        move_oval = [center_x, center_y, 10, 210, 0, speed, 0, 0]
    elif direction == 2:
        move_oval = [center_x, center_y, 10, 210, 0, -speed, 0, 0]
    else:
        init()
    return center_oval, move_oval


if __name__ == '__main__':
    root = Tk()

    WIDTH = 600
    HEIGHT = 600
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    c = Canvas(root, width=WIDTH, heigh=HEIGHT, bg="white")
    c.pack()

    speed = int(input("Введите скорость: "))

    inter = init()
    create_object(inter[0])
    e_id = create_object(inter[1])
    animate()
    root.mainloop()

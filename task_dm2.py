from drawman import *
from time import sleep

def coordinate_grid(n):
    """"""
    to_point(-300//n, 300//n)
    for i in range(0, 600//n+1, 100//n):
        pen_down()
        on_vector(0, -600//n)
        pen_up()
        on_vector(100//n, 600//n)
    to_point(-300//n, 300//n)
    for i in range(0, 600//n, 100//n):
        pen_down()
        on_vector(600//n, 0)
        pen_up()
        on_vector(-600//n, -100//n)
    to_point(0, 0)

def f(x):
    return x*x

n=20
drawman_scale(n)
coordinate_grid(n)
x=-5.0
to_point(x, f(x))
pen_down()
while x<=5:
    to_point(x, f(x))
    x+=0.1
pen_up()
sleep(10)

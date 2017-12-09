#
# CS1010S --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    "your answer here"

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def reflect_through_x_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(x_of(pt), -y_of(pt))
    return reflected_curve

def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))
    return reflected_curve

def snowflake():
    base = kochize(5)
    down = reflect_through_x_axis(base)
    intermediate = connect_ends(down, reflect_through_y_axis(rotate(pi/3)(base)))
    return connect_ends(half, reflect_through_y_axis(rotate(-pi/3)(base)))

#draw_connected_scaled(10000, snowflake())

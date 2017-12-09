#
# CS1010S --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# unit_circle returns make_point(sin(2*pi*t), cos(2*pi*t)), for t values between 0 and 1.

# alternative_unit_circle returns make_point(sin(2*pi*t**t), cos(2*pi*t*t)), for t values between 0 and 1.

# If we mathematically observe the squares of decimal numbers from 0 to 1, they are closer together near to 0 and get more spaced out as they get closer to 1. This explains the observation that the points for unit_circle are all evenly spaced(due to unit increment), whereas the points for alternative_unit_circle get more and more spaced out as t gets closer and closer to 1.

##########
# Task 2 #
##########

# (a)
def spiral(t):
	
	return make_point(t*sin(2*pi*t), t*cos(2*pi*t))

# draw_connected_scaled(1000, spiral)

# (b)

def relect_through_y_axis(curve):
        def reflected_curve(t):
            pt = curve(t)
            return make_point(-x_of(pt), y_of(pt))
        return reflected_curve
        
def heart(t):
    return connect_rigidly(spiral,reflect_through_y_axis(spiral))

# draw_connected_scaled(1000, heart)

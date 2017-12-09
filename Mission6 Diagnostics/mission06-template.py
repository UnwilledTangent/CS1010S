#
# CS1010S --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:







# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: gosper_curve(50)(0), 500)

# Time measurements
#  148, 204, 171, 154, 152
#  Average = 165.8


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: gosper_curve_with_angle(50, lambda lvl: pi/4)(0), 500)

# Time Measurements
#  152, 230, 156, 201, 189
#  Average = 185.6

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: your_gosper_curve_with_angle(50, lambda lvl: pi/4)(0), 500)

# Time Measurements
#  15259, 14442, 14389, 15116, 14461
#  Average = 14733.4


# Conclusion:
# your_gosper_curve_with_angle took significantly longer than both gosper_curve_with_angle and gosper_curve.
# gosper_curve, which was the most specialized function, took the shortest time, followed by gosper_curve_with_angle,
# which is less specialized becuase it takes in an additional input, namely the angle. The most generalized function,
# your_gosper_curve_with_angle, took the longest time. This tells us that specialized functions have a faster runtime
# than generalized functions.

##########
# Task 2 #
##########

# 1) 
# Yes, joe_rotate works and achieve the same purpose as rotate. While they are implemented slightly differently,
# joe_rotate still accesses the same x and y values from the curve and returns the same thing.

# 2) 
#Analysis of rotate:
# Pre assigning the variable, then accessing its x and y values using x_of(pt) and y_of(pt) is
# linear. This is because x_of(pt) and y_of(pt) extract the values from the initialised point. This linear 
# step is done once in the entire function.

# Analysis of joe_rotate:
# In this function, pt is not initialised. Instead, to access the x and y values, the function has to call x_of() and
# y_off() on curve(t) twice, so this linear step is done twice.

# Overall Analysis for gosper_curve:
# gosper_curve returns repeated(gosperize, level)(unit_line) and gosperize calls the rotation function (either rotate
# or joe_rotate) twice within it. When joe_rotate is used, the extra linear steps within it get compounded in
# the recursive process of calling repeated(gosperize, level). Thus the total time complexity is exponential for
# joe_rotate.

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <...>         <...>
#                      2         <...>         <...>
#                      3         <...>         <...>
#                      4         <...>         <...>
#                      5         <...>         <...>
#
#  Evidence of exponential growth in joe_rotate.
trace(x_of)
gosper_curve(1)(0.5)
untrace(x_of)
gosper_curve(1)(0.5)

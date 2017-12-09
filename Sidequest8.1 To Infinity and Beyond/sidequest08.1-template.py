#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> Noth
def get_velocity_component(angle, velocity):
    angle = pi*angle/180
    v_y = velocity * sin(angle)
    v_x = velocity * cos(angle)
    return (v_x, v_y)

# print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
	acc_x, acc_y = 0, 0
	for planet in planets:
		a_x, a_y = calculate_single_acceleration(planet, current_x, current_y)
		acc_x = acc_x + a_x
		acc_y = acc_y + a_y
	return acc_x, acc_y

def calculate_single_acceleration(planet, current_x, current_y):
	p_x, p_y = get_x_coordinate(planet), get_y_coordinate(planet)
	r = sqrt((p_x - current_x)**2 + (p_y - current_y)**2)
	M = get_mass(planet)
	a_x = (G * M * (p_x - current_x)) / r**3
	a_y = (G * M * (p_y - current_y)) / r**3
	return (a_x, a_y)

# print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    vx, vy = Y[2], Y[3]
    ax, ay = calculate_total_acceleration(planets, Y[0], Y[1])
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
#print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(80.5, 27.1)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)

#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic, n):
    if n == 1:
        return pic
        
    return beside(pic, fractal(stackn(2, pic), n-1))

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    if n == 1: return pic
    
    res = stackn(2**(n-1), pic)
    for i in range(n-1, 1, -1):
        res = beside(stackn(2**(i-1), pic), res)
    
    return beside(pic, res)

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    if n == 1:
        return pic1
    return beside(pic1, dual_fractal(stackn(2, pic2), stackn(2, pic1), n-1))

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(pic1, pic2, n):
    if n == 1:
		return pic1
		
	if n%2 == 0:
		res = stackn(2**(n-1), pic2)
	elif n%2 == 1:
		res = stackn(2**(n-1), pic1)
		
	for i in range(n-1, 1, -1):
		if i%2 == 0:
			res = beside(stackn(2**(i-1), pic2), res)
		elif i%2 == 1:
			res = beside(stackn(2**(i-1), pic1), res)
			
	return beside(pic1, res)
    
# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(a,b,c,d):
    return mosaic(overlay_frac(3/4, blank_bb, a), overlay_frac(1/2, blank_bb, b), overlay_frac(1/4, blank_bb, c), d)

def mosaic(pic1, pic2, pic3, pic4):
    return stack(beside(pic4,pic1), beside(pic3,pic2))

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))



def test2(pic1, pic2, n):
    if n == 1:
        return pic1
    elif n == 2:
        return beside(pic1,stack(pic2,pic2))
    else:
        if n%2 == 0:
            counter = 0
            y = pic2
        else:
            counter = 1
            y = pic1
        x = pic2 
        for i in range(n-1):
            if counter == 0:
                y = stack(y,y)
                x = beside(pic1,y)
                y = x
                counter += 1
                n -= 1
            else:
                y = stack(y,y)
                x = beside(pic2,y)
                y = x
                counter -= 1
                n -= 1
        return y

def test(pic1, pic2, n):
        if n == 1:
		return pic1
		
	if n%2 == 0:
		res = stackn(2**(n-1), pic2)
	elif n%2 == 1:
		res = stackn(2**(n-1), pic1)
		
	for i in range(n-1, 1, -1):
		if i%2 == 0:
			res = beside(stackn(2**(i-1), pic2), res)
		elif i%2 == 1:
			res = beside(stackn(2**(i-1), pic1), res)
			
	return beside(pic1, res)



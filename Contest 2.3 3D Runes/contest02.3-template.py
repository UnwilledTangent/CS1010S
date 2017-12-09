#
# CS1010S --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
def create_tile(n=10, pic=black_bb):
    pic = scale_independent(1, 1/6, black_bb)
    res = translate(0, 0.42, pic)
    y = 0.32
    for i in range(9):
        res = overlay_frac(2/9, translate(0,y,pic), res)
        y -= 0.1
    return res

def fifty_shades_of_gray(tile, n=5):
    if n == 1:
        return tile
    return stack(beside(tile, tile), fifty_shades_of_gray(stackn(n-1, tile), n-1))
    
hollusion(fifty_shades_of_gray(create_tile()))

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.
def get_peak(n=25, pic=circle_bb):
    res = pic
    for i in range(2, n+1):
        layer = scale((n+1-i)/n, pic)
        res = overlay_frac(1/i, layer, res)
    return res

def abstract_art(peak):
    res = peak
    for i in range(5):
        x,y = uniform(-1,1), uniform(-1,1)
        layer = translate(x, y, peak)
        res = overlay_frac(1/8, layer, res)
    return res

peak = get_peak()
anaglyph(abstract_art(peak))


# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)

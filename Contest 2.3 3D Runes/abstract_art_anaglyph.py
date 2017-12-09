from runes import *
from random import *

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


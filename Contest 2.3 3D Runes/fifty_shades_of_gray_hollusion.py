from runes import *

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


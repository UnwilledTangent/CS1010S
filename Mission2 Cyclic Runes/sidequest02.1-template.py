def tree(n, pic):
    res = pic
    for i in range(2, n+1):
        layer = scale((n+1-i)/n, pic)
        res = overlay_frac(1/i, layer, res)
    return res

def tree2(n, pic):
    if n == 1:
        return pic
    return overlay_frac((n-1)/n, tree(n-1, scale((n-1)/n, pic)), pic)


def helix(n, pic):
    pic = scale(2/n, pic)
    angle = pi + (2*pi/n)
    x, y = (math.sin(angle)*(0.5-1/n)), (math.cos(angle) * (0.5-1/n))
    res = translate(x, -y, pic)
    for i in range(2, n+1):
        angle = math.pi + 2*(math.pi)*i/n
        x = (math.sin(angle) * (0.5-(1/n)))
        y = (math.cos(angle) * (0.5-(1/n)))
        layer = translate(x,-y,pic)
        res = overlay_frac(1/i, layer, res)
    return res
    

def helix1(n, pic):
    pic = scale(2/n, pic)
    increment, r = 2*(math.pi)/n, 0.5-1/n
    res = translate(0,r,pic)
    for i in range(1, n+1):
        angle = i*increment
        x, y = (math.sin(angle)*(0.5-1/n)), (math.cos(angle) * (0.5-1/n))
        layer = translate(-x, y, pic)
        res = overlay_frac(1/i, layer, res)
    return res


def helix2(n, pic):
    pic = scale(2/n, pic)
    res = translate(0, 0.5-1/n ,pic)
    for i in range(1, n+1):
        angle = math.pi + (2*math.pi*i/n)
        x = (math.sin(angle) * (0.5-(1/n)))
        y = (math.cos(angle) * (0.5-(1/n)))
        layer = translate(x,-y,pic)
        res = overlay_frac(1/i, layer, res)
    return res
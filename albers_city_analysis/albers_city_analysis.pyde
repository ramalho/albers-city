from collections import namedtuple

larg_cel = 18.9
alt_cel = larg_cel
off = 5

vermelhos = []
beges = []

cores = dict(vermelho=(179, 29, 17), bege=(236, 218, 196), preto=(0,0,0))

def setup():
    size(1040, 530)
    # The background image must be the same size as the parameters
    # into the size() method. In this program, the size of the image
    # is 640 x 360 pixels.
    global bg
    bg = loadImage("josef-albers.png")
    noStroke()
    
# def draw():
    background(bg)
    for j in range(28):
        print '%2d' % j,
        for i in range(55):
            x0, y0, l, a = i*larg_cel, j*alt_cel, 10, 10
            cor = cor_media(x0+off, y0+off, l, a)
            fill(*cores[cor])
            rect(x0, y0, larg_cel, alt_cel)
            #if i != 36: 
            print cor[0],
        print
    #print(tupla_media(vermelhos))
    #print(tupla_media(beges))
    

def rgb(cor):
    r = cor >> 16 & 0xFF
    g = cor >> 8 & 0xFF
    b = cor & 0xFF
    return r, g, b

#def mouseMoved():
#    print(rgb(get(mouseX, mouseY)))    

def tupla_media(lista):
    return tuple(float(sum(l))/len(lista) for l in zip(*lista))

def cor_media(x0, y0, l, a):
    cores = []
    x0, y0 = int(x0), int(y0)
    for x in range(x0, x0+l, 2):
        for y in range(y0, y0+a, 2):
            cores.append(rgb(get(x, y)))
    amostras = len(cores)
    r, g, b = tupla_media(cores)
    if r > 150 and g < 150 and b < 150:
        cor = 'vermelho'
        #vermelhos.append((r, g, b))
    elif r > 150 and g > 150 and b > 150:
        #beges.append((r, g, b))
        cor = 'bege'
    else:
        cor = 'preto' 
    return cor
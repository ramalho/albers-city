mapa = """
pppppvvvvpppppppppbbbppppppppppppppppppppppppppbbbbbpb
pppppbbbbppppppppppppppppppvvvvvvvvppppppppbbbbbbbbbbb
pppppvvvvppppppvvvbbbpppppppppppppppppvvpppppppbbbbbpb
pppppbbbbppppppppppppppppbbvvvvvvvvppppppppbbbbbbbbbbb
pppppvvvvpppppbvvvbbbvvvvvvppppbbbbbbbvvpppppppbbbbbpb
pppppbbbbvvvvvvbbbpppppppbbvvvvvvvvppppppppbbbbpppppbb
pbbbbpppppppvvbvvvbbbvvvvvvppppbbbbbbbvvvvbvvvvbbbbbpb
pppppbbbbvvvvvvbbbpppppppbbvvvvvvvvpppppvvpbbbbpppppbb
pbbbbpppppppvvbvvvbbbvvvvvvppppbbbbbbbvvvvbvvvvbbbbbpb
pppppbbbbvvvvvvbbbpppppppbbvvvvvvvvpppppvvpbbbbpppppbb
pbbbbpppppppvvbvvvbbbvvvvvvppppbbbbbbbvvvvbvvvvbbbbbpb
pppppvvvvvvvvvvbbbpppppppvvvvvvvvvvpppppvvpbbbbpppppbb
pbbbbpppppppvvbvvvbbbvvvvvvbbbbbbbbbbbvvvvbvvvvbbbbbpb
pppppvvvvvvvvvvbbbvvvvvvvvvvvvvvvvvpppppvvpbbbbpppppbb
ppppppppppppbbbvvvbbbbbbbbbbbbbbbbbbbbbbbbbvvvvbbbbbbb
pppppbbbbbbbbbbbbbbbbbbbbbbvvvvvvvvbbbbbbbpbbbbpbbbbbb
pppppbbbbbbbbbbvvvbbbbbbbbbbbbbbbbbbbbbbbbbvvvvbbbbbbb
pppppbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbpbbbbbb
""".strip().split()

from collections import namedtuple

i_cels = len(mapa[0])
j_cels = len(mapa)
larg_cel = 20

cores = dict(v=(179, 29, 17), b=(236, 218, 196), p=(0,0,0))

def setup():
    size(1080, 360)
    print('size(%d, %d)' % (i_cels * larg_cel, j_cels * larg_cel))
    print(i_cels, j_cels)
    noStroke()
    
    for i in range(i_cels):
        for j in range(j_cels):
            cor = mapa[j][i]
            fill(*cores[cor])
            rect(i*larg_cel, j*larg_cel, larg_cel, larg_cel)
            
    save('cidade.png')
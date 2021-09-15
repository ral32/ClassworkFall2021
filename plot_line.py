def line(coord1, coord2, x3):
    b = coord1[1]-(coord1[0]*((coord2[1]-coord1[1])/(coord2[0]-coord1[0])))
    y3 = ((coord2[1]-coord1[1])/(coord2[0]-coord1[0]))*x3 + b
    return y3

def select(mat, point0, point1):
    xmax = max(point0[0], point1[0])
    xmin = min(point0[0], point1[0])

    ymax = max(point0[1], point1[1])
    ymin = min(point0[1], point1[1])

    print(xmin, ":", xmax)
    print(ymin, ":", ymax)

    return mat[ymin:ymax, xmin:xmax]

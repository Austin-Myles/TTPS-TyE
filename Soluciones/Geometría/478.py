import sys

def point_in_box(x, y, tl_x, tl_y, br_x, br_y):
    return tl_x < x < br_x and br_y < y < tl_y

def point_in_circle(x, y, c_x, c_y, r):
    return (x - c_x) ** 2 + (y - c_y) ** 2 < r ** 2

def sign(p1x, p1y, p2x, p2y, p3x, p3y):
    return (p1x - p3x) * (p2y - p3y) - (p2x - p3x) * (p1y - p3y)

def point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):
    d1 = sign(x, y, x1, y1, x2, y2)
    d2 = sign(x, y, x2, y2, x3, y3)
    d3 = sign(x, y, x3, y3, x1, y1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)

def main():
    output = []
    figuras = {}
    figura_count = 1
    punto_count = 1
    for line in sys.stdin:
        aux_line = line.strip().split()
        if aux_line[0] == "*": # Leemos los puntos
            break
        else:
            figura = aux_line[0] # Leemos la figura
            if figura == "r":    
                tl_x, tl_y = float(aux_line[1]), float(aux_line[2])
                br_x, br_y = float(aux_line[3]), float(aux_line[4])
                figuras[figura_count] = [tl_x, tl_y, br_x, br_y]
            elif(figura == "c"):
                x, y = float(aux_line[1]), float(aux_line[2])
                r = float(aux_line[3])
                figuras[figura_count] = [x, y, r]
            elif(figura == "t"):
                x1, y1 = float(aux_line[1]), float(aux_line[2])
                x2, y2 = float(aux_line[3]), float(aux_line[4])
                x3, y3 = float(aux_line[5]), float(aux_line[6])
                figuras[figura_count] = [x1, y1, x2, y2, x3, y3]
            figura_count += 1
    for line in sys.stdin:
        aux_line = line.strip().split()
        if aux_line[0] == "9999.9" and aux_line[1] == "9999.9":
            break
        else:
            x, y = float(aux_line[0]), float(aux_line[1])
            cant = 0
            for key, value in figuras.items():
                if len(value) == 4:
                    if(point_in_box(x, y, value[0], value[1], value[2], value[3])):
                        output.append(f"Point {punto_count} is contained in figure {key}")
                        cant += 1
                elif len(value) == 3:
                    if(point_in_circle(x, y, value[0], value[1], value[2])):
                        output.append(f"Point {punto_count} is contained in figure {key}")
                        cant += 1
                elif len(value) == 6:
                    if(point_in_triangle(x, y, value[0], value[1], value[2], value[3], value[4], value[5])):
                        output.append(f"Point {punto_count} is contained in figure {key}")
                        cant += 1
            if cant == 0:
                output.append(f"Point {punto_count} is not contained in any figure")
            punto_count += 1
    print("\n".join(output))
if __name__ == "__main__":
    main()
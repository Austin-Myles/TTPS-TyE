import sys

def main():
    output = []
    for line in sys.stdin:
        aux = "The gopher cannot escape."
        cant = 0
        line_aux = line.strip().split()
        cases = int(line_aux[0])
        gx, gy = float(line_aux[1]), float(line_aux[2])
        dx, dy = float(line_aux[3]), float(line_aux[4])
        for _ in range(cases):
            x, y = map(float, sys.stdin.readline().strip().split())
            goph_dist = ((gx - x) ** 2 + (gy - y) ** 2) ** 0.5
            dog_dist = ((dx - x) ** 2 + (dy - y) ** 2) ** 0.5
            if (goph_dist <= dog_dist / 2) and (cant == 0):
                aux = ("The gopher can escape through the hole at ({:.3f},{:.3f}).".format(x, y))
                cant += 1
        output.append(aux)
        sys.stdin.readline()
        
    print("\n".join(output))
if __name__ == "__main__":
    main()
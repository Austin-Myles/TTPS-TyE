import sys

def main():
    output = [] # Como siempre, el output se guarda en una lista
    for line in sys.stdin: # Recorremos cada linea del input
        aux = "The gopher cannot escape."
        cant = 0 # Lo utilizamos para contar la cantidad de veces que la tuza escapa
        line_aux = line.strip().split()
        cases = int(line_aux[0])
        gx, gy = float(line_aux[1]), float(line_aux[2]) # Tomamos las coordenadas de la tuza
        dx, dy = float(line_aux[3]), float(line_aux[4]) # Tomamos las coordenadas del perro
        for _ in range(cases): # Recorremos cada caso
            x, y = map(float, sys.stdin.readline().strip().split())
            goph_dist = ((gx - x) ** 2 + (gy - y) ** 2) ** 0.5
            dog_dist = ((dx - x) ** 2 + (dy - y) ** 2) ** 0.5
            if (goph_dist <= dog_dist / 2) and (cant == 0): # Solo vamos a hacer el append de la primera coordenada por la cual la tuza pueda escapar
                aux = ("The gopher can escape through the hole at ({:.3f},{:.3f}).".format(x, y))
                cant += 1
        output.append(aux)
        sys.stdin.readline()     
    print("\n".join(output))
if __name__ == "__main__":
    main()
import sys

def puntLinea(n, puntos):
    r = 0
    for i in range(n):
        m = []
        for j in range(i + 1, n):
            if puntos[i][0] != puntos[j][0]:  # Evitamos las lineas verticales
                pendiente = (puntos[i][1] - puntos[j][1]) / (puntos[i][0] - puntos[j][0])
            else:  # En el caso de que sea una linea vertical la pendiente es infinita
                pendiente = float('inf')
            m.append(pendiente)
        
        # Ordenamos las pendientes
        m.sort()
        
        t = 1
        for k in range(1, len(m)):
            if abs(m[k] - m[k - 1]) < 1e-6:
                t += 1
            else:
                r = max(r, t)
                t = 1
        r = max(r, t)
    return r + 1

def main():
    output = []
    cases = int(sys.stdin.readline().strip())  # Leemos el número de casos
    sys.stdin.readline()  # Ignoramos la línea en blanco entre casos
    
    for _ in range(cases):
        puntos = []  # Guardamos los puntos en una lista
        for line in sys.stdin:
            aux_line = line.strip()
            if not aux_line: # Recorremos hasta llegar al blanco
                break
            x, y = map(float, aux_line.split())
            puntos.append((x, y))
        
        output.append(str(puntLinea(len(puntos), puntos)))
        output.append("")
    for i in range(len(output) - 1): # Por motivos de presentación lo imprimimos con un for
        print(output[i])

if __name__ == "__main__":
    main()

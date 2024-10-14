import heapq

# TIME LIMIT EXCEDED

while True:
    try:
        n = int(input())

        pila = []
        cola = []
        prio = []

        es_cola = True
        es_pila = True
        es_prio = True

        for x in range(n):
            op = list(map(int, input().split()))
            
            if op[0] == 1:
                pila.append(op[1])
                cola.append(op[1])
                heapq.heappush(prio, - op[1])

            elif op[0] == 2:
                if pila:
                    if op[1] != pila.pop():
                        es_pila = False
                else:
                    es_pila = False
                
                if cola:
                    if op[1] != cola.pop(0):
                        es_cola = False
                else:
                    es_cola = False
                
                if prio:
                    if op[1] != -heapq.heappop(prio):
                        es_prio = False
                else:
                    es_prio = False
            
        posibilidad = es_prio + es_cola + es_pila

        if posibilidad == 0:
            print("impossible")
        elif posibilidad > 1:
            print("not sure")
        else:
            if es_cola:
                print("queue")
            elif es_pila:
                print("stack")
            else:
                print("priority queue")
                
    except(EOFError):
        break
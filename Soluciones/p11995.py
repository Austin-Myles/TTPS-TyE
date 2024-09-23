
while True:
    try:
        n = int(input())
        aux_queue = []
        aux_cola = []
        aux_prio = []
        cola = True
        pila = True
        prio = True
        for x in range(n):
            op = list(map(int, input().split()))
        
            if op[0] == 1:
                if cola:
                    aux_queue.append(op[1])
                


        """
        if(cola and (not pila and not prio)):
            print("queue")
        elif(pila and (not cola and not prio)):
            print("stack")
        elif(prio and (not cola and not pila)):
            print("priority queue")
        elif(not prio and (not cola and not pila)):
            print("imposible")
        else:
            print("not sure")
        """
    except(EOFError):
        break
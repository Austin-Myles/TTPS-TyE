def main():
    while True:
        try:
            lista = list(map(int, input().split()))
            df = lista.pop(0)
            # All values in this array are false
            values = [False] * (df - 1)
            for i in range(1, len(lista)):
                diff = abs(lista[i] - lista[i - 1])
                if diff < df:
                    if values[diff - 1] == True:
                        break
                    else:    
                        values[diff - 1] = True
            if all(values):
                print("Jolly")

            if False in values:
                print("Not jolly")
        except EOFError:
            break


if __name__ == '__main__':
    main()
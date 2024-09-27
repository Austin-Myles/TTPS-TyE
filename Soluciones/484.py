lista = list(map(int, input().split()))
dicc = {}
for x in range(len(lista)):
    if lista[x] in dicc:
        dicc[lista[x]] += 1
    else:
        dicc[lista[x]] = 1

for key, value in dicc.items():
    print(f"{key} {value}")
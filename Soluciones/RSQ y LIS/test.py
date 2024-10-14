class Elephant:
    def __init__(self, weight, iq, index):
        self.weight = weight
        self.iq = iq
        self.index = index

# Leer los elefantes
elephants = []
index = 1
w, iq = map(int, input().split())
while w:
    elephants.append(Elephant(w, iq, index))
    index += 1
    w, iq = map(int, input().split())

# Ordenar los elefantes por peso (ascendente) y en caso de empate, por IQ (descendente)
elephants.sort(key=lambda e: (e.weight, -e.iq))

# Ahora aplicamos LIS pero sobre la inteligencia decreciente
n = len(elephants)
dp = [1] * n
prev = [-1] * n

# LIS sobre IQ decreciente
for i in range(n):
    for j in range(i):
        if elephants[j].iq > elephants[i].iq and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

# Encontrar la longitud máxima de la subsecuencia y reconstruir la secuencia
max_len = 0
last_index = -1
for i in range(n):
    if dp[i] > max_len:
        max_len = dp[i]
        last_index = i

# Reconstruir la subsecuencia
sequence = []
while last_index != -1:
    sequence.append(elephants[last_index].index)
    last_index = prev[last_index]

# Imprimir el resultado
print(max_len)
for idx in reversed(sequence):
    print(idx)

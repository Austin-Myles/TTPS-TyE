#RUNTIME ERROR
dicc = {}
words = list(input().split())
while words and len(dicc) < 100000:
    dicc.update({words[1]: words[0]})
    words = list(input().split())
    if not words:
        break

word = input()
output = []
while word and len(output) < 100000:
    if word in dicc:
        output.append(dicc[word])
    else:
        output.append("eh")
    word = input()

for x in range(len(output)):
    print(output[x])
print("")
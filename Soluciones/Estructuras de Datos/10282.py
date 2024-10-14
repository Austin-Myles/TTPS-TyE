#RUNTIME ERROR
import sys

dicc = {}
lines = sys.stdin.readlines()

for line in lines:
    words = line.split()
    if not words:
        break
    dicc[words[1]] = words[0]

for word in lines[len(dicc)+1:]:
    word = word.strip()
    if word in dicc:
        print(dicc[word])
    else:
        print("eh")

        
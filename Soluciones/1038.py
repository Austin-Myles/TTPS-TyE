# -*- coding: utf-8 -*-

snack = {'1': 4.00, '2': 4.50, '3': 5.00, '4': 2.00, '5': 1.50}

X, Y = input().split()
total = snack[X] * int(Y)
print(f"Total: R$ {total:.2f}")

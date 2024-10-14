def main():
    T = int(input())

    days = [0] * T

    for i in (range(T)):
        N = int(input())
        P = int(input())
        hartals = []
        for j in (range(P)):
            hartals.append(int(input()))
        days[i] = 0
        for j in range(1, N + 1):
            if j % 7 == 6 or j % 7 == 0:
                continue
            for h in hartals:
                if j % h == 0:
                    days[i] += 1
                    break
    for i in days:
        print(i)

if __name__ == '__main__':
    main()
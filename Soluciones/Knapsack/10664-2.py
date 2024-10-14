import sys
import typing as t

def lcs_length(seq1: t.Sequence[t.Any], k: int) -> int:
    N = len(seq1) + 1
    K = k + 1
    cache = [0 for _ in range(N * K)]

    for i in range(1, N):
        row_i = i * K
        for j in range(1, K):
            if seq1[i - 1] > j:
                cache[row_i + j] = cache[row_i - K + j]
                continue

            cache[row_i + j] = max(cache[row_i -K + j], cache[row_i - K +(j-seq1[i-1])] + seq1[i-1])

    return cache[N * K -1]


lines = sys.stdin.readlines()
line_i = 0
lines_len = int(lines[0])
r = ""
while lines_len > 0:
    lines_len -= 1
    line_i += 1
    weights = tuple(int(w) for w in lines[line_i].split())

    total_w = sum(weights)
    if total_w % 2 > 0:
        r+= 'NO\n'
        continue

    target = total_w // 2
    o = lcs_length(weights, target)
    if o == target:
        r+= 'YES\n'
    else:
        r+= 'NO\n'

sys.stdout.write(r)
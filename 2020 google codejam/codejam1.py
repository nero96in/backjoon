import sys

T = int(sys.stdin.readline())

results = []
for i in range(T):
    mat = []
    N = int(sys.stdin.readline())
    x = i+1
    k = 0
    r = 0
    c = 0
    for _ in range(N):
        row1 = list(map(int, sys.stdin.readline().replace('\n', '').split()))
        if len(set(row1)) != N: r += 1
        mat.append(row1)
    
    transposed_mat = list(map(list, zip(*mat)))
    for diagonal_idx, row2 in enumerate(transposed_mat):
        if len(set(row2)) != N: c += 1
        k += row2[diagonal_idx]

    results.append("Case #{}: {} {} {}".format(x, k, r, c))

for result in results: print(result)
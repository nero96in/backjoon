import sys

def candidates(mat, i, j, N, K):
    candidates = [e for e in range(1, N+1)]
    candidates = candidates[::-1]

    for k in range(N):
        # print("i:", i, "j:", j, "k:", k)
        if mat[i][k] in candidates: candidates.remove(mat[i][k])
        if mat[k][j] in candidates: candidates.remove(mat[k][j])
    
    if i == j:
        traces = 0
        temp = []
        for t in range(N):
            if i != t: traces += mat[t][t]
        for candidate in candidates:
            if traces + candidate <= K: temp.append(candidate)
        candidates = temp
    
    return candidates

def trace_check(mat, N, K):
    traces = 0
    for t in range(N): traces += mat[t][t]
    if traces == K: return True
    else: return False
        
def dfs(mat, i, j, N, K):
    promisings = candidates(mat, i, j, N, K)
    # print("i:", i, "j:", j, "promisings:", promisings)
    for num in promisings:
        # print("i:", i, "j:", j, "Current promise:", num, "Current mat:", mat)
        mat[i][j] = num
        # print(mat)
        if i == N-1 and j == N-1:
            if trace_check(mat, N, K): return True, mat
            else:
                mat[i][j] = 0
                return False, None
        if j == N-1:
            next_i = i + 1
            next_j = 0
        else:
            next_i = i
            next_j = j + 1
        flag, result = dfs(mat, next_i, next_j, N, K)
        if flag: return True, result
        mat[i][j] = 0
        # print("end loop of {} {}:".format(i, j), mat)
    return False, None

T = int(sys.stdin.readline())

results = []
for i in range(T):
    # for N in range(2, 6):
    #     for K in range(1*N, N*N+1):
    N, K = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    # print(N, K)
    mat = [[0 for _ in range(N)] for _ in range(N)]
    flag, mat_result = dfs(mat, 0, 0, N, K)
    results.append((flag, mat_result))
    # results.append("Case #{}: {}".format(i+1, message))

for x, result in enumerate(results):
    flag, mat_result = result
    if flag:
        message = "POSSIBLE"
        print("Case #{}: {}".format(x+1, message))
        for row in mat_result:
            print(*row, sep=" ")
    else:
        message = "IMPOSSIBLE"
        print("Case #{}: {}".format(x+1, message))
T = int(input())

results = []
for _ in range(T):
    A, B = map(int, input().split())
    results.append(A+B)

for result in results: print(result)
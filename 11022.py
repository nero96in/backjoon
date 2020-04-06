import sys

T = int(input())
for x in range(1, T+1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print("Case #{}: {} + {} = {}".format(x, A, B, A+B))
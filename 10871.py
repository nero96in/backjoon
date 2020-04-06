import sys

N, X = map(int, input().split())
nums = list(map(int, input().split()))
result = [a for a in nums if a < X]
print(*result, sep=" ")
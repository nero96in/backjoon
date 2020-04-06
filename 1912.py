import sys

n = int(sys.stdin.readline())
num_set = list(map(int, sys.stdin.readline().split()))

# n 크기의 리스트로 dp 초기화
dp = [None for _ in range(n)]
dp[0] = num_set[0]

for i in range(1, n):
    # 더한 값과, 주어진 수열의 값(대각선 값) 비교 
    if dp[i-1] + num_set[i] > num_set[i]:
        dp[i] = dp[i-1] + num_set[i]
    else: dp[i] = num_set[i]

result = max(dp)

print(result)
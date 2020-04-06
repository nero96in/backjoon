import sys

N, L = map(int, sys.stdin.readline().split())

# 홀수개의 연속된 숫자의 평균은 항상 정수이고.
# 짝수개의 연속된 숫자의 평균은 항상 정수.5 이다.
# 평균 * 연속된 숫자의 개수 = N
# 평균 = N / 연속된 숫자의 개수

results = []
for length in range(L, 101):
    if length % 2 == 1: # 홀수
        if N % length == 0: # 나누어 떨어짐, 몫이 정수
            median = int(N / length)
            min_result = median - (length - 1) // 2
            if min_result < 0: break # 수열에 음수가 포함됨.
            max_result = median + (length - 1) // 2
            for result in range(min_result, max_result+1):
                results.append(result)
            break

    elif length % 2 == 0: # 짝수
        value = N / length
        if (value - int(value)) == 0.5: # 나눈 값의 소수 부분이 0.5일 때.
            min_result = int(value - 0.5) - (length // 2 - 1)
            if min_result < 0: break # 수열에 음수가 포함됨.
            max_result = int(value + 0.5) + (length // 2 - 1)
            for result in range(min_result, max_result+1):
                results.append(result)
            break

if results:
    print(" ".join(map(str, results)))
else:
    print(-1)

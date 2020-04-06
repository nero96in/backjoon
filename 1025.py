import sys
import math

M, N = map(int, sys.stdin.readline().split())

numbers = []
for _ in range(M):
    numbers.append(list(map(int, list(sys.stdin.readline().replace('\n', '')))))

result = -1

for m in range(M): # 어느 행에서 시작할 것인가?
    for n in range(N): # 어느 열에서 시작할 것인가?
        for weight_m in range(-M, M): # 행에서의 공차. -M부터 시작
            for weight_n in range(-N, N): # 열에서의 공차. -N부터 시작
                # 두 공차가 모두 0이면 무한 루프
                if weight_m == 0 and weight_n == 0: continue
                step = 0
                x = m
                y = n
                value = ''
                # 입력받은 수들의 범위 안에서 가능한 수열 추출
                while (0 <= x < M) and (0 <= y < N):
                    # 숫자 조합을 하고
                    value += str(numbers[x][y]))
                    step += 1

                    # 제곱수이고, 최댓값 갱신이 가능한지 확인
                    value_int = int(''.join(value))
                    value_sqrt = math.sqrt(value_int)
                    value_decimal = value_sqrt - int(value_sqrt)
                    if value_decimal == 0 and value_int > result: result = value_int

                    x = m + step * weight_m
                    y = n + step * weight_n

print(result)
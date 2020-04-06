import sys

cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
cnt_dict = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5, 9],
    6: [0, 6],
    7: [8]
}

def count_lines(digits):
    total_lines = 0
    for digit in digits: total_lines += cnt[int(digit)]
    return total_lines

digits = sys.stdin.readline().replace('\n', '')
N = len(digits)

max_ans = int("1"+"0"*N)
ans = max_ans
for i in range(N):
    target_digits = digits[-(i+1)]
    total_lines = count_lines(target_digits)

    if i == 0:
        # 일의 자리 숫자보다 큰 숫자 중, 선분 수가 같은 숫자 찾기
        cur_target = int(digit[-1])
        cur_target_cnt = cnt[cur_target]
        same_cnts = cnt_dict[cur_target_cnt]
        for c in same_cnts:
            if c > cur_target:
                ans = digit[:-1] + str(c)
                break
        if ans != max_ans: break

print(ans)
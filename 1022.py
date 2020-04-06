import sys
import time

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

four_edges = [(r1, c1), (r2, c1), (r1, c2), (r2, c2)]

max_level = max(abs(r1), abs(r2), abs(c1), abs(c2))
# min_level = min(abs(r1), abs(r2))
if r1 * r2 < 0: min_level = 0

result = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
max_length = 0

for level in range(max_level-50, max_level+1):
    coord = [level, level]
    value = (2 * level + 1) ** 2

    if level == 0:
        if r1 <= coord[0] <= r2 and c1 <= coord[1] <= c2:
            result[coord[0]-r1][coord[1]-c1] = value
            continue
    
    # 시작 지점에서 왼쪽으로 이동
    for i1 in range(level * 2):
        if r1 <= coord[0] <= r2 and c1 <= coord[1] <= c2:
            result[coord[0]-r1][coord[1]-c1] = value
            # 저장된 값들 중, 가장 긴 길이를 가진 숫자의 길이를 계속해서 갱신
            if len(str(value)) > max_length: max_length = len(str(value))
        coord[1] -= 1
        value -= 1
    
    # 그 다음 위쪽으로 이동
    for i2 in range(level * 2):
        if r1 <= coord[0] <= r2 and c1 <= coord[1] <= c2:
            result[coord[0]-r1][coord[1]-c1] = value
            # 저장된 값들 중, 가장 긴 길이를 가진 숫자의 길이를 계속해서 갱신
            if len(str(value)) > max_length: max_length = len(str(value))
        coord[0] -= 1
        value -= 1

    # 그 다음 오른쪽으로 이동
    for i3 in range(level * 2):
        if r1 <= coord[0] <= r2 and c1 <= coord[1] <= c2:
            result[coord[0]-r1][coord[1]-c1] = value
            # 저장된 값들 중, 가장 긴 길이를 가진 숫자의 길이를 계속해서 갱신
            if len(str(value)) > max_length: max_length = len(str(value))
        coord[1] += 1
        value -= 1

    # 그 다음 아래쪽으로 이동
    for i4 in range(level * 2):
        if r1 <= coord[0] <= r2 and c1 <= coord[1] <= c2:
            result[coord[0]-r1][coord[1]-c1] = value
            # 저장된 값들 중, 가장 긴 길이를 가진 숫자의 길이를 계속해서 갱신
            if len(str(value)) > max_length: max_length = len(str(value))
        coord[0] += 1
        value -= 1
        

print_format = "{0:>" + str(max_length+1) + "}"
for row in result:
    row_print = ""
    for val in row:
        row_print += print_format.format(str(val))
    if row_print[0] == " ": sys.stdout.write(row_print[1:] + "\n")
    else: sys.stdout.write(row_print + "\n")
import sys

N = int(sys.stdin.readline())

schedules = []
timer = 0
for _ in range(N):
    s = tuple(map(int, sys.stdin.readline().replace("\n", "").split()))
    schedules.append(s)

selected = []
# 종료 시각 -> 시작 시각 순으로 정렬
schedules = sorted(schedules, key=lambda x: (x[1], x[0]))
for schedule in schedules:
    if schedule[0] < timer: continue
    selected.append(schedule)
    timer = schedule[1]

print(len(selected))
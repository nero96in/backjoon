import sys

T = int(sys.stdin.readline())

results = []
for i in range(T):
    N = int(sys.stdin.readline())
    Cameron = []
    James = []
    schedules = []
    for _ in range(N): schedules.append(tuple(map(int, sys.stdin.readline().replace('\n', '').split())))
    result = [s for s in schedules]
    schedules = sorted(schedules, key=lambda x: (x[0], x[1]))
    for idx, schedule in enumerate(schedules):
        original_idx = result.index(schedule)
        if not Cameron or Cameron[-1][1] <= schedule[0]:
            Cameron.append(schedule)
            result[original_idx] = "C"
        elif not James or James[-1][1] <= schedule[0]:
            James.append(schedule)
            result[original_idx] = "J"
        else:
            result = "IMPOSSIBLE"
            break
    
    if result != "IMPOSSIBLE": result = "".join(result)

    results.append("Case #{}: {}".format(i+1, result))

for result in results: print(result)
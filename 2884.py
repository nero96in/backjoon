H, M = map(int, input().split())

total_M = 60 * H + M
if total_M >=45: alarm = total_M - 45
else: alarm = 1440 + total_M - 45

print("{} {}".format(alarm // 60, alarm % 60))
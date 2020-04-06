N = input()
if len(N) < 2: N = "0"*(2-len(N)) + N
cycle = 0
new_N = N
while True:
    cycle += 1
    new_N = new_N[-1] + str(sum(map(int, list(new_N))))[-1]
    if new_N == N: break

print(cycle)
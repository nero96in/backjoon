count = [0 for _ in range(10)]
total = 1
for _ in range(3): total *= int(input())
for num in str(total): count[int(num)] += 1
for c in count: print(c)
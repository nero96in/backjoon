burgers = []
baberages = []
for _ in range(3): burgers.append(int(input()))
for _ in range(2): baberages.append(int(input()))

print(min(burgers) + min(baberages) - 50)
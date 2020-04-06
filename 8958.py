T = int(input())
for _ in range(T):
    OX = input()
    total = 0
    score = 0
    for ox in OX:
        if ox == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)
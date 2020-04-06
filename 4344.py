C = int(input())
for _ in range(C):
    scores = list(map(int, input().split()))[1:]
    avg = sum(scores) / len(scores)
    count = 0
    for score in scores:
        if score > avg: count += 1
    print("{0:.3f}%".format(count / len(scores) * 100))
import sys

T = int(sys.stdin.readline())

results = []
for i in range(T):
    depth = 0
    S = list(sys.stdin.readline().replace('\n', ''))
    result = ""
    for idx in range(len(S)):
        digit = int(S[idx])
        delta = digit - depth
        if delta > 0:
            paren = "(" * delta
            result += (paren + str(digit))
        elif delta == 0:
            result += str(digit)
        else:
            paren = ")" * abs(delta)
            result += (paren + str(digit))
        depth = digit
        if idx == len(S) - 1: result += ")" * depth
    results.append("Case #{}: {}".format(i+1, result))

for result in results: print(result)
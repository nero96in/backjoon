N = int(input())
if N == 1: print("*")
else:
    odd_stars = ["*" if i % 2 == 0 else " " for i in range(N)]
    even_stars = ["*" if j % 2 == 1 else " " for j in range(N)]
    for _ in range(N):
        print(*odd_stars, sep="")
        print(*even_stars, sep="")
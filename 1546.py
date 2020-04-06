N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

scores = [score/max_score*100 for score in scores]
print(sum(scores)/N)
import sys

def dfs(x, y):
    global visited
    global base
    global amount
    global N

    if not base[x][y]: return False
    # 일단 방문한 집은 방문했다고 표시한다.
    visited[x][y] = True
    # 변을 공유하는 집끼리는 간선으로 연결되어 있다고 본다.
    adjacents = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    for ax, ay in adjacents:
        # 변을 공유하는 집의 좌표가 범위 내에 있는 경우에
        if 0 <= ax < N and 0 <= ay < N:
            # 집이 있지만 방문하지 않은 정점이 있으면
            if base[ax][ay] and not visited[ax][ay]:
                # 단지의 크기를 1 늘리고
                amount += 1
                # 그 정점에 또 연결된 단지가 없는지 탐색(DFS)한다.
                dfs(ax, ay)
        
N = int(sys.stdin.readline())
visited = [[False for _ in range(N)] for _ in range(N)]
groups = []
base = []
for _ in range(N):
    base.append(list(map(int, sys.stdin.readline().replace("\n", ""))))

for x in range(N):
    for y in range(N):
        # x, y에 집이 있고 방문하지 않은 정점이라면
        if base[x][y] and not visited[x][y]:
            # 먼저 단지 크기를 1로 시작하고
            amount = 1
            # 그 집 주변에 인접한 집이 없는지 탐색한다.
            dfs(x, y)
            # 탐색이 끝나면 계산된 단지 크기를 답 목록에 넣는다.
            groups.append(amount)

print(len(groups))
groups.sort()
for i in groups:
    print(i)
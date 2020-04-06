import sys

def bfs(maze, N, M):
    depth = 0
    queue = [(0, 0)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    while queue:
        # 다음 Depth의 Queue를 위한 임시 리스트
        next_queue = []
        depth += 1
        # print("depth", depth, ":", queue)
        if (N-1, M-1) in queue: break
        for x, y in queue:
            if x == N-1 and y == M-1: break
            visited[x][y] = True
            adjacents = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for ax, ay in adjacents:
                if 0 <= ax < N and 0 <= ay < M:
                    if maze[ax][ay] and not visited[ax][ay]:
                        visited[ax][ay] = True
                        # 이런식으로 모아둔 뒤에
                        next_queue.append((ax, ay))
        # 다음 Depth의 Queue로 업데이트 합니다.
        queue = next_queue
    
    return depth

N, M = map(int, sys.stdin.readline().split())

maze = []
for _ in range(N): maze.append(list(map(int, sys.stdin.readline().replace('\n', ''))))
print(bfs(maze, N, M))
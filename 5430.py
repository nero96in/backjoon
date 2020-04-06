import sys
import json

def AC(p, n, deque):
    # D의 개수가 수의 개수보다 많으면 에러
    if p.count("D") > n: return "error"
    # 수열을 최종으로 뒤집어야 하는지 여부 확인
    if p.count("R") % 2 == 0: final_reverse = False
    else: final_reverse = True
    
    # 수를 빼낼 방향 결정
    direction = 0
    for f in p:
        # R을 만나면 방향 변경
        if f == "R":
            if direction == 0: direction = -1
            else: direction = 0
        # D를 만나면 방향에 해당하는 수를 빼냄
        else: deque.pop(direction)
    
    # 최종으로 뒤집어야하면 뒤집음
    if final_reverse: deque.reverse()

    deque = str(deque).replace(" ", "")
    return deque

T = int(sys.stdin.readline())
results = []
for _ in range(T):
    p = list(sys.stdin.readline().replace('\n', ''))
    n = int(sys.stdin.readline())
    
    # 리스트 형태로 바로 입력받는게 아니라 str 형식으로 입력받게 됨.
    # 이걸 리스트로 바꿔야하는데 가장 간단한 방법은 json 형식으로 읽는 것이라고 판단.
    deque = json.loads(sys.stdin.readline().replace('\n', ''))
    results.append(AC(p, n, deque))

for result in results:
    sys.stdout.write(str(result)+'\n')
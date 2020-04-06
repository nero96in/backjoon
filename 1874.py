import sys

n = int(sys.stdin.readline())
num_list = []
for _ in range(n): num_list.append(int(sys.stdin.readline()))

stack = []
progress = []
one_to_n = [i for i in range(1, n+1)]
while num_list:
    # 할 수 있는 행동이 없으면 만들 수 없는 수열임.
    if not one_to_n and stack[-1] != num_list[0]:
        progress = ["NO"]
        break

    # 스택이 비어있으면 다음 숫자를 넣기
    if not stack:
        stack.append(one_to_n.pop(0))
        progress.append("+")
    
    # 스택에 있는 마지막 숫자가 만들어야 할 수열의 첫번째 숫자와 같다면
    if stack[-1] == num_list[0]:
        # 스택과 만들 수열의 첫번째 숫자를 빼내기(삭제)
        stack.pop()
        progress.append("-")
        num_list.pop(0)
    # 그렇지 않으면
    else:
        # 스택에 다음 숫자를 넣기
        stack.append(one_to_n.pop(0))
        progress.append("+")

    
for i in progress: sys.stdout.write(str(i)+'\n')
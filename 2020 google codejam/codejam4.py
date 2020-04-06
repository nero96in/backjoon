import sys

T, B = map(int, sys.stdin.readline().replace("\n", "").split())

def make_candidates(digits):
    A = []
    for e1 in digits:
        if e1 == 0: A.append(1)
        elif e1 == 1: A.append(0)
        else: A.append(None)
    B2 = digits[::-1]
    C = []
    for e2 in B2:
        if e2 == 0: C.append(1)
        elif e2 == 1: C.append(0)
        else: C.append(None)
    D = digits
    return [A, B2, C, D]

search_order_base = []
for num in range(int(B/2)):
    search_order_base.append(num)
    search_order_base.append(B-num-1)
# print(search_order_base)

results = []
for _ in range(T):
    result = [None for _ in range(B)]
    visited = [False for _ in range(B)]
    search_order = [s for s in search_order_base]
    for step in range(150):
        # print("step:", step)
        if step < 10 or step % 10 > 1:
            cur_idx = search_order.pop(0)
            visited[cur_idx] = True
            print(cur_idx+1)
            sys.stdout.flush()
            answer = int(input())
            result[cur_idx] = answer
            # print(result)
            # print(search_order)
        elif step % 10 == 0: # 바뀐 직후 (2개만 거름)
            candidates = make_candidates(result)
            next_candidates = []
            # print("candidates:", candidates)
            print(1)
            sys.stdout.flush()
            answer = int(input())
            for candidate in candidates:
                if candidate[0] == answer: next_candidates.append(candidate)
            candidates = [nc for nc in next_candidates]
            # print("next condidates:", candidates)
        elif step % 10 == 1: # 바뀐 내용 확정
            candidates1, candidates2 = candidates
            if candidates1 == candidates2:
                result = [c1 for c1 in candidates1]
                print(1)
                sys.stdout.flush()
                _ = int(input())
                # print("ommiting and modified result:", result)
            else:
                comparing_idx = None
                for idx in range(B):
                    if candidates1[idx] != candidates2[idx]:
                        comparing_idx = idx
                        break
                print(comparing_idx+1)
                sys.stdout.flush()
                answer = int(input())
                if answer == candidates1[comparing_idx]: result = [c1 for c1 in candidates1]
                else: result = [c2 for c2 in candidates2]
            # print("modified result:", result)
        # 1 0 0 1 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 
        if None not in result: break

    print("".join(list(map(str, result))))
    sys.stdout.flush()
    final_answer = str(input())
    if final_answer == "Y": continue
    else: break
            

    # for i in range(1, B+1):
    #     print(i)
    #     sys.stdout.flush()
    #     answer = str(input())
    #     result[i] = answer
    # print("".join(result[1:]))
    # sys.stdout.flush()
    # result = str(input())
    # if result == "Y": continue
    # else: break
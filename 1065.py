def is_han(n):
    if len(str(n)) <= 2: return True
    nums = list(map(int, list(str(n))))
    a = nums[0]
    delta = nums[1] - nums[0]
    for i in range(len(nums)):
        if nums[i] != a + delta * i: return False
    return True

N = int(input())
count = 0
for i in range(1, N+1):
    if is_han(i): count+=1

print(count)
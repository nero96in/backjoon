nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

max_num = max(nums)
max_idx = nums.index(max_num)
print(max_num)
print(max_idx+1)
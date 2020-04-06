nums = [i for i in range(1, 10001)]
for j in range(10000):
    dn = j + sum(map(int, list(str(j))))
    if dn in nums: nums.remove(dn)
for num in nums: print(num)
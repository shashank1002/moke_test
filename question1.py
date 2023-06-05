nums = list(map(int,input()[1:-1].split(',')))
for i in range(len(nums)):
    if nums[i] == 0:
        nums.remove(0)
        nums.insert(len(nums),0)
print(nums)
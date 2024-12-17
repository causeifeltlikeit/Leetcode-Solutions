nums = [3,2,4]
target = 6

numsHash = {}
for i in range(len(nums)):
    comp = target - nums[i]
    if comp in numsHash:
        print(numsHash[comp])
        print(i)
        break
    numsHash[nums[i]] = i
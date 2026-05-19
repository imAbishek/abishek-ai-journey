nums = [3, 8, 12, 2, 7]
target = 9

seen = {}

for index, num in enumerate(nums):
    numExist = target - num
    if numExist in seen:
        print(seen[numExist], index)
    else:
        seen[num] = index

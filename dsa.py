from fontTools.misc.cython import returns

nums = [3, 8, 12, 2, 7]
target = 9

seen = {}

for index, num in enumerate(nums):
    numExist = target - num
    if numExist in seen:
        print(seen[numExist], index)
    else:
        seen[num] = index


s = "listen"
t = "silent"

sortedS = sorted(s)
sortedT = sorted(t)

if sortedS == sortedT:
    print("true")
else:
    print("false")

memoryS = {}

for char in s:
    if char in memoryS:
        memoryS[char] += 1
    else:
        memoryS[char] = 1

memoryT = {}

for char in t:
    if char in memoryT:
        memoryT[char] += 1
    else:
        memoryT[char] = 1

if memoryS == memoryT:
    print("true")
else:
    print("false")


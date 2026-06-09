nums = [1,2,3,1]
seen = set()

for num in nums:
    if num in seen:
        print(True)
    seen.add(num)
print(False)
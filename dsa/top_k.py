nums = [1,1,1,2,2,3]
k = 2

seen = {}

for num in nums:
    if num in seen:
        seen[num] += 1
    else:
        seen[num] = 1

results = sorted(seen.keys(), key=lambda p: seen[p], reverse=True)
results = results[:k]
print(results)
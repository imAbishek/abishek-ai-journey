strs = ["eat","tea","tan","ate","nat","bat"]

seen = {}

for stir in strs:
    memory = "".join(sorted(stir))
    if memory in seen:
        seen[memory].append(stir)
    else:
        seen[memory] = [stir]

    print(seen[memory])
nums = [1, 2, 3, 4]

# left = []
# right = []
# runningLeft = 1
# runningRight = 1
#
# for num in nums:
#     left.append(runningLeft)
#     runningLeft = runningLeft * num
# print(left)
#
# for num in nums[::-1]:
#     right.append(runningRight)
#     runningRight = runningRight * num
# right = right[::-1]
# print(right)
#
# answer = []
# for i in range(len(left)):
#     answer.append(left[i] * right[i])
# print(answer)

# for i, num in enumerate(nums):
#     product = 1
#     for j, num2 in enumerate(nums):
#         if i != j:
#             product *= num2
#     result.append(product)

# print(result)

n = len(nums)
answer = [1] * n

running = 1
for i in range(n):
    answer[i] = running
    running *= nums[i]
print(answer)

running = 1
for i in range(n - 1, -1, -1):
    print(i)
    answer[i] *= running
    running *= nums[i]

print(answer)




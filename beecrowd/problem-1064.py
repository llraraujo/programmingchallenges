
nums = []

positives = []

nums.append(float(input()))
nums.append(float(input()))
nums.append(float(input()))
nums.append(float(input()))
nums.append(float(input()))
nums.append(float(input()))


for num in nums:
    if num >= 0:
        positives.append(num)

media = sum(positives)/len(positives)

print(f'{len(positives)} valores positivos')
print(f'{media:.1f}')

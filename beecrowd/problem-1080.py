numbers = []

for num in range(0, 100):
    numbers.append(int(input()))

max_number = max(numbers)
position_max_number = numbers.index(max_number) + 1

print(f'{max_number}\n{position_max_number }')

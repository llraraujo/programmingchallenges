
i = 1
j = 7
count = 0
while i + j <= 16:
    print(f'I={i} J={j}')
    j -= 1
    count += 1
    if count == 3:
        i += 2
        j = 7
        count = 0



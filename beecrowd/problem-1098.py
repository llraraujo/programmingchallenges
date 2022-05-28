
i = 0
j = 0
count = 0
r = 0.2
while i < 2:
    j += 1
    count += 1
    if i == 0 or i == 1 or i > 1.8:
        print(f'I={i:.0f} J={j:.0f}')
    else:
        print(f'I={i:.1f} J={j:.1f}')
    if count == 3:
        i += 0.2
        j = j - 3 + 0.2
        count = 0

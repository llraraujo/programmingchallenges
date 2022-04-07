
N = int(input())

minutes = 0
hours = 0
seconds = N

while seconds >= 60:
    seconds -= 60
    minutes += 1
    if(minutes >= 60):
        hours += 1
        minutes -= 60




print(f'{hours}:{minutes}:{seconds}')
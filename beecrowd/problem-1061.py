
foo = input().split()

time = input().split(":")

day_start = int(foo[1]) * 24 * 60 * 60

hour_start = int(time[0]) * 60 * 60

minute_start = int(time[1]) * 60

second_start = int(time[2])

total_start_time_seconds = day_start + hour_start + minute_start + second_start

foo = input().split()

time = input().split(":")

day_end = int(foo[1]) * 24 * 60 * 60

hour_end = int(time[0]) * 60 * 60

minute_end = int(time[1]) * 60

second_end = int(time[2])

total_end_time_seconds = day_end + hour_end + minute_end + second_end

duration_event_seconds = total_end_time_seconds - total_start_time_seconds

day_event = duration_event_seconds // (60 * 60 * 24)

duration_event_seconds = duration_event_seconds % (60 * 60 * 24)

hour_event = duration_event_seconds // (60 * 60)

duration_event_seconds = duration_event_seconds % (60 * 60)

minute_event = duration_event_seconds // 60

seconds_event = duration_event_seconds % 60

print(f'{day_event} dia(s)\n{hour_event} hora(s)\n{minute_event} minuto(s)\n{seconds_event} segundo(s)')

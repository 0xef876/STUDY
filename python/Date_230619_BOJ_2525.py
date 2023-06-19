hour , minute = map(int, input().split())
time = int(input())

minute += time
if minute >= 60:
    hour += minute//60
    minute = minute%60


if hour >= 24:
    hour = hour%24

print(hour, minute)
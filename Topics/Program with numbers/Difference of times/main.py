# put your python code here
hour_walk = int(input())
minutes_walk = int(input())
seconds_walk = int(input())
time_walk = (hour_walk * 3600) + (minutes_walk * 60) + (seconds_walk * 1)

hour_rain = int(input())
minutes_rain = int(input())
seconds_rain = int(input())
time_rain = (hour_rain * 3600) + (minutes_rain * 60) + (seconds_rain * 1)

print(time_rain - time_walk)

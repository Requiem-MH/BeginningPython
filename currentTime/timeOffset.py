import time

#current time
currentTime = time.time()

mins = 60
secs = 60
hour = mins * secs

#Calculate different time zone into seconds
zoneTime = int(input("Enter the time zone offset to GMT (+/-): ")) * hour

#Total Seconds
totalSeconds = int(currentTime + zoneTime)

#Current Seconds
currentSeconds = totalSeconds % 60

#Total mins
totalMinutes = totalSeconds // 60

#Current minutes in the hour
currentMinutes = totalMinutes % 60

#Total Hours
totalHours = totalMinutes // 60

#Current hour
currentHour = totalHours % 24

#Display current time in different time zone


print("The current time is", currentHour, ":", currentMinutes, ":", currentSeconds)


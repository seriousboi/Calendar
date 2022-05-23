import time


monthsNames = ["January","February","March","April","May","June","July","August","September","October","November","December"]
monthsDurations = [31,28,31,30,31,30,31,31,30,31,30,31]


def getDate():
    global monthsDurations

    #jour 0: 1 mai 2022
    originDay = 19113

    epochTimeSec = int(time.time())
    epochTimeSec += 60*60*2 #deux fuseaux de décalage avec GMT
    epochTimeMin = epochTimeSec//60
    epochTimeHour = epochTimeMin//60
    epochTimeDays = epochTimeHour//24

    day = epochTimeDays - originDay
    day += 0

    month = 4
    year = 2022
    monthsWeekStart = 6
    increment = 0

    while day > increment + monthsDurations[month]:
        increment += monthsDurations[month]
        if month == 11:
            year += 1
        monthsWeekStart = (monthsWeekStart+monthsDurations[month])%7
        month = (month+1)%12

    monthDay = day-increment

    return day,month,year,monthDay,monthsWeekStart

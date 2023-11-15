from calculus import *


def getThingsTodo():
    global monthsNames

    thingsTodo = []
    thingsTodoBefore = []

    try:
        file = open("data/events.txt","r",encoding='utf-8')
        lines = file.readlines()
        file.close()

        for lineIndex in range(len(lines)):
            if lineIndex%2 == 0:

                infoLine = lines[lineIndex].split()
                eventType = int(infoLine[0])
                if eventType == 1:

                    thingTodo = "["+infoLine[3]+" "+monthsNames[int(infoLine[2])-1]+" "+infoLine[1]+"] "+lines[lineIndex+1][0:-1]
                    thingsTodoBefore += [thingTodo]

                if eventType == 0:

                    thingTodo = lines[lineIndex+1][0:-1]
                    #changer codex
                    thingsTodo += [thingTodo]

    except FileNotFoundError:
        pass

    thingsTodo = thingsTodoBefore + thingsTodo
    return thingsTodo


def getBirthdays(day,month,year):
    birthdays = []

    try:
        file = open("data/birthdays.txt","r",encoding='utf-8')
        lines = file.readlines()
        file.close()

        for lineIndex in range(len(lines)):
            if lineIndex%2 == 0:

                    dateTxt = lines[lineIndex].split()
                    if month+1 == int(dateTxt[1]) and day+1 == int(dateTxt[0]):

                        birthday = lines[lineIndex+1][0:-1]
                        birthdays += [birthday]

    except FileNotFoundError:
        pass

    return birthdays


def getDayEvents(day,month,year):
    events = []

    try:
        file = open("data/events.txt","r",encoding='utf-8')
        lines = file.readlines()
        file.close()

        for lineIndex in range(len(lines)):
            if lineIndex%2 == 0:

                infoLine = lines[lineIndex].split()
                eventType = int(infoLine[0])
                if eventType == 1 or eventType == 2:

                    if year == int(infoLine[1]) and month+1 == int(infoLine[2]) and day+1 == int(infoLine[3]):

                        event = lines[lineIndex+1][0:-1]
                        events += [event]

    except FileNotFoundError:
        pass

    return events


def getDayScore(day,month,year):
    try:
        txt = get_txt_list("data/scoremem.txt")
        for line in txt:
            if int(line[0]) == year and int(line[1]) == month+1 and int(line[2]) == day+1:
                if len(line) >= 5:
                    dayAmount = int(line[4])
                else:
                    dayAmount = None
                return int(line[3]),dayAmount

    except FileNotFoundError:
        pass

    return None,None


def setDayScore(day,month,year,score,amount):
    try:
        file = open("data/scoremem.txt","r")
        lines = file.readlines()
        file.close()

        if score == None:
            score = 2
        if amount == None:
            amount = ""
        newLine = [str(year)+" "+str(month+1)+" "+str(day+1)+" "+str(score)+" "+str(amount)+"\n"]
        newLines = newLine + lines

        file= open("data/scoremem.txt","w")
        file.writelines(newLines)
        file.close()

    except FileNotFoundError:
        pass


def get_txt_list(filename):
    file = open(filename,"r")
    lines = file.readlines()
    txt_list = []
    for line_index in range(len(lines)):
        txt_list += [lines[line_index].split()]
    file.close()
    return txt_list

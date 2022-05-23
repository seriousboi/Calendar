from display import *
from calculus import *
from storage import *
import pygame


def calendar():
    global monthsDurations

    pygame.init()
    window = pygame.display.set_mode((560,560))
    pygame.display.set_caption("Calendar")
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.QUIT])

    day,month,year,monthDay,monthsWeekStart = getDate()
    currentMonth = month
    currentYear = year

    while True:
        previousHitbox,nextHitbox,todoHitbox,daysHitboxes = drawMonth(window,monthDay,currentMonth,currentYear,month,year,monthsWeekStart)
        pygame.display.update()
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            pygame.display.quit()
            return

        elif event.type == pygame.MOUSEBUTTONDOWN:

            for monthDay2 in range(monthsDurations[currentMonth]):
                if daysHitboxes[monthDay2].collidepoint(event.pos):
                    dayInfos(window,monthDay2,currentMonth,currentYear)

            if todoHitbox.collidepoint(event.pos):
                thingsTodo(window)

            if previousHitbox.collidepoint(event.pos):
                monthsWeekStart = (monthsWeekStart-monthsDurations[currentMonth-1])%7
                if currentMonth == 0:
                    currentYear -= 1
                currentMonth = (currentMonth-1)%12
            if nextHitbox.collidepoint(event.pos):
                monthsWeekStart = (monthsWeekStart+monthsDurations[currentMonth])%7
                if currentMonth == 11:
                    currentYear += 1
                currentMonth = (currentMonth+1)%12


def thingsTodo(window):
    while True:
        backHitbox = drawThingsTodo(window)
        pygame.display.update()
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            pygame.display.quit()
            return

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if backHitbox.collidepoint(event.pos):
                return


def dayInfos(window,day,month,year):
    while True:
        backHitbox,setHitbox = drawDay(window,day,month,year)
        pygame.display.update()
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            pygame.display.quit()
            return

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if backHitbox.collidepoint(event.pos):
                return

            elif setHitbox.collidepoint(event.pos):
                setScore(window,day,month,year)


def setScore(window,day,month,year):
    pygame.draw.rect(window,mainColor(),(120,410,320,80),0)
    pygame.draw.rect(window,tertiaryColor(),(120,410,320,80),1)
    text(window,"P",35,(100,200,150),"center",120+40,410+40)
    text(window,"S",35,(250,250,200),"center",120+40+80*1,410+40)
    text(window,"F",35,(225,75,75),"center",120+40+80*2,410+40)
    text(window,"H",35,(50,25,25),"center",120+40+80*3,410+40)
    pygame.display.update()

    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        pygame.display.quit()
        return

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.Rect(120,410,80,80).collidepoint(event.pos):
            setDayScore(day,month,year,0)
        if pygame.Rect(120+80,410,80,80).collidepoint(event.pos):
            setDayScore(day,month,year,1)
        if pygame.Rect(120+80*2,410,80,80).collidepoint(event.pos):
            setDayScore(day,month,year,2)
        if pygame.Rect(120+80*3,410,80,80).collidepoint(event.pos):
            setDayScore(day,month,year,3)

    pygame.draw.rect(window,secondaryColor(),(120,470,320,80),0)


calendar()

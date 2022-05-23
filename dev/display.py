from calculus import *
from storage import *
import pygame


def drawThingsTodo(window):

    window.fill(quaternaryColor())

    backHitbox = text(window,"back",25,tertiaryColor(),"topright",540,20)

    index = 0
    for thing in getThingsTodo():
        text(window,thing,20,tertiaryColor(),"topleft",10,80+index*30)
        index += 1

    return backHitbox


def drawDay(window,day,month,year):
    global monthsNames

    window.fill(secondaryColor())

    date = str(day+1)+" "+monthsNames[month]+" "+str(year)
    text(window,date,30,tertiaryColor(),"topleft",20,20)

    backHitbox = text(window,"back",25,tertiaryColor(),"topright",540,20)

    setHitbox = text(window,"set score",25,tertiaryColor(),"bottomright",540,540)

    index = 0
    for birthday in getBirthdays(day,month,year):
        text(window,birthday+" birthday",25,tertiaryColor(),"topleft",20,80+index*40)
        index += 1
    for event in getDayEvents(day,month,year):
        text(window,event,25,tertiaryColor(),"topleft",20,80+index*40)
        index += 1

    return backHitbox,setHitbox


def drawMonth(window,monthDay,currentMonth,currentYear,month,year,monthsWeekStart):
    global monthsNames, monthsDurations

    window.fill(mainColor())
    pygame.draw.rect(window,secondaryColor(),(0,0,560,80),0)

    if month == currentMonth and year == currentYear:
        x = (monthDay+monthsWeekStart)%7
        y = (monthDay+monthsWeekStart)//7
        pygame.draw.rect(window,(250,225,100),(x*80,y*80+80,80,80),0)

    text(window,monthsNames[currentMonth],30,tertiaryColor(),"center",280,40)
    text(window,str(currentYear),15,tertiaryColor(),"center",280,65)

    previousHitbox = text(window,"<",30,tertiaryColor(),"center",160,40)
    nextHitbox = text(window,">",30,tertiaryColor(),"center",400,40)

    todoHitbox = text(window,"to do",25,tertiaryColor(),"topleft",15,15)
    pygame.draw.rect(window,quaternaryColor(),todoHitbox,0)
    pygame.draw.rect(window,tertiaryColor(),todoHitbox,1)
    text(window,"to do",25,tertiaryColor(),"topleft",15,15)

    pygame.draw.rect(window,tertiaryColor(),(0,80,560-1,480-1),2)
    for x in range(6):
        pygame.draw.line(window,tertiaryColor(),(80+80*x,80),(80+80*x,560))
    for y in range(5):
        pygame.draw.line(window,tertiaryColor(),(0,160+80*y),(560,160+80*y))

    daysHitboxes = []
    for day in range(monthsDurations[currentMonth]):
        x = (day+monthsWeekStart)%7
        y = (day+monthsWeekStart)//7

        daysHitboxes += [pygame.Rect(x*80,y*80+80,80,80)]

        text(window,str(day+1),12,tertiaryColor(),"topleft",x*80+5,y*80+5+80)

        if getBirthdays(day,currentMonth,currentYear) != []:
            text(window,"!",35,quinaryColor(),"topright",x*80+77,y*80+80)
        if getDayEvents(day,currentMonth,currentYear) != []:
            text(window,"!",35,quaternaryColor(),"bottomright",x*80+77,y*80+80+77)

        dayScore = getDayScore(day,currentMonth,currentYear)

        if dayScore == None:
            pass
        elif dayScore == 0:
            text(window,"P",25,(100,200,150),"center",x*80+40,y*80+40+80)
        elif dayScore == 1:
            text(window,"S",25,(250,250,200),"center",x*80+40,y*80+40+80)
        elif dayScore == 2:
            text(window,"F",25,(225,75,75),"center",x*80+40,y*80+40+80)
        elif dayScore == 3:
            text(window,"H",25,(50,25,25),"center",x*80+40,y*80+40+80)

    return previousHitbox,nextHitbox,todoHitbox,daysHitboxes


def text(window,message,size,color,anchor,x,y):

    font = pygame.font.SysFont("verdana", size)
    text = font.render(message,True,color)
    area = text.get_rect()
    width = area.width
    height = area.height

    vect= {"topleft":[0,0],
           "bottomleft":[0,-2],
           "topright":[-2,0],
           "bottomright":[-2,-2],
           "midtop":[-1,0],
           "midleft":[0,-1],
           "midbottom":[-1,-2],
           "midright":[-2,-1],
           "center":[-1,-1]}

    x = x + vect[anchor][0]*width/2
    y = y + vect[anchor][1]*height/2

    return window.blit(text,(x,y))


def mainColor():
    return (250,175,75)


def secondaryColor():
    return (150,175,250)


def tertiaryColor():
    return (70,70,70)


def quaternaryColor():
    return (50,230,150)


def quinaryColor():
    return (255,125,225)

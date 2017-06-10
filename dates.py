weekdays = {0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday" }

# determines the day of the week a particular date falls on, based on the fact that 2015-10-28 is a Wednesday
# date must be string in the form yyyy-mm-dd
def dayOfWeek(date):
    
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])

    monthsReg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    iterYear = 2015
    iterMonth = 10
    iterDay = 28

    tot = 0
    
    while(True):
        if(leapYear(iterYear)):
            months = monthsLeap
        else:
            months = monthsReg
            
        while(iterMonth < 13):
            while(iterDay < months[iterMonth-1]+1):
                if(iterYear == year and iterMonth == month and iterDay == day):
                    return (tot+3) % 7
                iterDay += 1
                tot += 1
            iterDay = 1
            iterMonth += 1
        iterMonth = 1
        iterYear += 1

# determines whether a year is a leap year
# year: an int
def leapYear(year):
    return year % 4 == 0 and (not(year % 100 == 0) or (year % 400 == 0))

# lists all the dates between two specified dates, inclusive
# start and end must be strings in the form yyyy-mm-dd
def listAllDates(start, end):

    retList = []

    days = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    
    monthsReg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    startYear = int(start.split('-')[0])
    startMonth = int(start.split('-')[1])
    startDay = int(start.split('-')[2])

    endYear = int(end.split('-')[0])
    endMonth = int(end.split('-')[1])
    endDay = int(end.split('-')[2])
    
    leapStart = startYear % 4 == 0 and (not(startYear % 100 == 0) or (startYear % 400 == 0))
    leadEnd = endYear % 4 == 0 and (not(endYear % 100 == 0) or (endYear % 400 == 0))

    iterYear = startYear
    iterMonth = startMonth
    iterDay = startDay

    while(True):
        if(leapYear(iterYear)):
            months = monthsLeap
        else:
            months = monthsReg
            
        while(iterMonth < 13):
            while(iterDay < months[iterMonth-1]+1):
                retList.append(str(iterYear) + '-' + str(iterMonth) + '-' + str(iterDay))
                if(iterYear == endYear and iterMonth == endMonth and iterDay == endDay):
                    return retList
                iterDay += 1
            iterDay = 1
            iterMonth += 1
        iterMonth = 1
        iterYear += 1

# lists all the dates in a particular range that fall on particular days of the week
# start & end: strings in the form "yyyy-mm-dd"
# day: a list of ints corresponding to the day (starting with 0 for Sunday)
# returns: goodDates, a list of dictionaries in the form {date:dayofweek}, where date is a string in the form "yyyy-mm-dd"
#          and dayofweek is an int 0-6 representing the day of the week (0 is Sunday)
def listAllDays(start, end, day):
    dates = listAllDates(start, end)
    goodDates = []
    for i in dates:
        weekday = dayOfWeek(i)
        if(weekday in day):
            goodDates.append(i)
    return goodDates

class RehearsalDate:
    # date: string in the form "yyyy-mm-dd"
    # actorList: a list of strings that are actor names
    # sceneList: a list of strings that are scenes
    def __init__(self, date, actorList, sceneList):
        self.date = date
        self.day = dayOfWeek(date)
        self.actorList = actorList
        self.sceneList = sceneList

    def __str__(self):
        return "Date: " + self.date + "\nDay: " + weekdays[self.day] + "\nActors Available: " + str(self.actorList) + "\nScenes: " + str(self.sceneList) + "\n"

    def addActor(self, actor):
        self.actorList.append(actor)

    def addScene(self, scene):
        self.sceneList.append(scene)

    def removeActor(self, actor):
        for act in self.actorList:
            if act == actor:
                self.actorList.delete(act)

    def removeScene(self, scene):
        for scenes in self.sceneList:
            if scenes == scene:
                self.sceneList.delete(scenes)
    
        

            
        

import dates
import actor
import rehearsals
import scene


##john = actor.Actor("John","Man Who Can Sell Anything",[1, 3, 5], ["2015-11-16","2015-12-25"])
##
##print(john)
##
##rehearsalDates = dates.listAllDays("2015-11-9","2016-2-5",[1, 3, 4])
##rehearsalSchedule = []
## create rehearsal schedule
##for date in rehearsalDates:
##    actorList = []
##    newReh = rehearsals.RehearsalDate(date, [], [])
##    if(newReh.day in john.avail and newReh.date not in john.special):
##        newReh.addActor(john.name)
##        for sc in john.role.scenes:
##            newReh.addScene(sc)
##    rehearsalSchedule.append(newReh)
##
##for sched in rehearsalSchedule:
##    print(sched)

##def makeActorList():
##    actorList = []
##    actorsFile = open("Actors.csv")
##    actors = actorsFile.readlines()
##    actorsFile.close()
##
##    for act in actors:
##        fields = act.split(',')
##        actorList.append(actor.Actor(fields[0], fields[1], fields[2].split(), fields[3].split()))
##    return actorList
##
##def makeSceneList():
##    sceneList = []
##    sceneFile = open("Scenes.txt")
##    scenes = sceneFile.readlines()
##    sceneFile.close()
##
##    for sc in scenes:
##        fields = sc.split('\t')
##        chars = fields[1].split(', ')
##        for i in range(0,len(chars)):
##            chars[i] = chars[i].strip('"\n')
##        sceneList.append(scene.Scene(fields[0], chars))
##    return sceneList
##    
##actorsList = makeActorList()
##scenesList = makeSceneList()

days = dates.listAllDays("2016-09-04","2016-11-12",[0,2,4])
weekdays = {0:"Sun",
            2:"T",
            4:"Th" }
csvstring = ""
for i in range(0,len(days)):
    csvstring+=weekdays[dates.dayOfWeek(days[i])] + " " + days[i][5:] + ","
csvfile = open("days.csv", 'w')
csvfile.write(csvstring)
csvfile.close()
print(csvstring)
    
    


import dates

class RehearsalDate:
    # date: string in the form "yyyy-mm-dd"
    # actorList: a list of strings that are actor names
    # sceneList: a list of strings that are scenes
    def __init__(self, date, actorList, sceneList):
        self.date = date
        self.day = dates.dayOfWeek(date)
        self.actorList = actorList
        self.sceneList = sceneList

    def __str__(self):
        return "Date: " + self.date + "\nDay: " + dates.weekdays[self.day] + "\nActors Available: " + str(self.actorList) + "\nScenes: " + str(self.sceneList)

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

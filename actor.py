class Actor:
    # name: string
    # role: string
    # availability: list of ints (represents days of the week the actor is available)
    # special: list of strings in the form "yyyy-mm-dd" (represents special dates the actor is NOT available)
    def __init__(self, name, role, availability, special):
        self.name = name
        self.role = role
        self.avail = availability
        self.special = special

    def __str__(self):
        return self.name + ', ' + str(self.role) + ', ' + str(self.avail) + ', ' + str(self.special)

    # newAvail: list of ints (represents days of the week to add to the actors availability)
    def addAvailability(self, newAvail):
        for days in newAvail:
            if(not(days in self.avail)):
                self.avail.append(days)

    # newDel: list of ints (represents days of the week to remove from the actors availability)
    def removeAvailability(self, newDel):
        for days in newDel:
            if(days in self.avail):
                self.avail.delete(days)

    # newSpec: list of strings in the form "yyyy-mm-dd" (represents date to add to actor's unavailiabity)
    def addSpecial(self, newSpec):
        for dates in newSpec:
            if(not(dates in self.special)):
                self.special.append(dates)

    # delSpec: list of strings in the form "yyyy-mm-dd" (represents date to remove from actor's unavailability) 
    def removeSpecial(self, delSpec):
        for dates in delSpec:
            if(dates in self.special):
                self.special.delete(dates)

    


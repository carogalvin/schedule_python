class Scene:
    # number: string
    # characters: list of strings, representing character names
    def __init__(self, number, characters):
        self.number = number
        self.characters = characters

    def __str__(self):
        return self.number + ", " + str(self.characters)

    def addCharacter(self, char):
        self.characters.append(char)

    def removeCharacter(self, char):
        if(char in self.characters):
            self.characters.remove(char)

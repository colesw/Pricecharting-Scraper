class VideoGame:
    def __init__(self, id, title, console, loosePrice, completePrice, newPrice):
        self.id = id
        self.title = title
        self.console = console
        self.loosePrice = loosePrice
        self.completePrice = completePrice
        self.newPrice = newPrice

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    
    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getConsole(self):
        return self.console
    def setConsole(self, console):
        self.console = console

    def getLoosePrice(self):
        return self.loosePrice
    def setLoosePrice(self, loosePrice):
        self.loosePrice = loosePrice

    def getCompletePrice(self):
        return self.completePrice
    def setCompletePrice(self, completePrice):
        self.completePrice = completePrice

    def getNewPrice(self):
        return self.newPrice
    def setNewPrice(self, newPrice):
        self.newPrice = newPrice

    def printVals(self):
        print ("Id: {}\nTitle: {}\nConsole: {}\nLoose: ${}\nComplete: ${}\nNew: ${}\n\n".format(self.id,self.title, self.console, self.loosePrice, self.completePrice, self.newPrice))

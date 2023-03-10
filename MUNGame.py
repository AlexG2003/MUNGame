class Item:
    def __init__(self, itemName, itemDescription = ' '):
        self.__itemName = itemName
        self.__itemDescription = itemDescription
    def getName(self):
        return self.__itemName

    def getDescription(self):
        return self.__itemDescription
    
    def string(self):
        itemName = print("ItemName: " + self.__itemName)
        if self.__itemDescription != " ":
            itemDescription = print("Item Description:" + self.__itemDescription)

class Character:
    def __init__(self, characterName, characterRace = "Human", AttributeOne = "None", AttributeTwo = "None", itemCount = 0, healthBar = 100):
        self.__characterName = characterName
        self.__AttributeOne = AttributeOne
        self.__AttributeTwo = AttributeTwo
        self.__inventory = []
        self.__itemCount = itemCount
        self.__healthBar = healthBar
        self.__characterRace = characterRace

    def getName(self):
        return self.__characterName
    def setName(self, characterName = 'Unknown'):
        self.__characterName = characterName

    def getRace(self):
        return self.__characterRace
    def setRace(self, changeRace):
        self.__characterRace = changeRace
    
    def getAttributeOne(self):
        return self.__AttributeOne
    def setAttributeOne(self, newAttributeOne):
        self.__AttributeOne = newAttributeOne

    def getAttributeTwo(self):
        return self.__characterAttributeTwo
    def setAttributeTwo(self, newAttributeTwo):
        self.__AttributeTwo = newAttributeTwo

    def getInventory(self):
        return self.__inventory
    
    def getHealth(self):
        return self.__healthBar
    def setHealth(self, setHealth):
        self.__healthBar = setHealth
    
    def equipItem(self, item):
        if self.__itemCount < 9:
            if self.__itemCount == 8:
                self.__inventory.append(item)
                self.__itemCount += 1
                print("You have picked up")
                print("Inventory is now full")
            

            if self.__itemCount != 9:
                self.__inventory.append(item.getName())
                self.__itemCount += 1
                print(self.getName() + " has picked up " + item.getName(), end = "")
                if item.getDescription() != ' ':
                    print(": " + item.getDescription())
                if item.getDescription() == ' ':
                    print(" ")
        
        if self.__itemCount == 10:
            print("Inventory is full; please discard an item to pick this up")

    def dropItem(self, item):
        self.__inventory.remove(item.getName())
        print(self.getName() + " has dropped " + item.getName(), end = "")
        if item.getDescription() != ' ':
            print(": " + item.getDescription())
        if item.getDescription() == ' ':
            print(" ")

    def characterdesc(self):
        print("Characters Name: " + self.__characterName)
        print("Charcter Attributes:", self.__AttributeOne, end= '')
        if self.__AttributeOne != 'none' and self.__AttributeTwo != 'none':
            print(" &", self.__AttributeTwo)
        #Prevents 'None' from printing twice if the character has no attributes
        if self.__AttributeTwo == 'none':
            print(" ")
        print("Character's Inventory: ", end = ' ')
        print(self.getInventory())
        return ' '

    def lookInventory():
        print(" ")
        print("Opening inventory. . .")
        print(self.__inventory)

def main():
    ##Character creator##
    C1Name = input("Please input Character 1's Name: ")
    C1Race = input("Please input the race of Character 1: ")
    C1Atrribute1 = input("Please input Chracter 1's first attribute, enter 'none' if none: ")
    if C1Atrribute1 != 'none':
        C1Atrribute2 = input("Please input Chracter 1's second attribute, enter 'none' if none: ")
    if C1Atrribute1 == 'none':
        C1Atrribute2 = 'none'
    Character1 = Character(C1Name, C1Race, C1Atrribute1, C1Atrribute2, 0, 100)

    C2Name = input("Please input Character 2's Name: ")
    C2Race = input("Please input the race of Character 2: ")
    C2Atrribute1 = input("Please input Chracter 2's first attribute, enter 'none' if none: ")
    if C2Atrribute1 != 'none':
        C2Atrribute2 = input("Please input Chracter 2's second attribute, enter 'none' if none: ")
    if C2Atrribute1 == 'none':
        C2Atrribute2 = 'none'
    Character2 = Character(C2Name, C2Race, C2Atrribute1, C2Atrribute2, 0, 100)
        
    C3Name = input("Please input Character 3's Name: ")
    C3Race = input("Please input the race of Character 3: ")
    C3Atrribute1 = input("Please input Chracter 3's first attribute, enter 'none' if none: ")
    if C3Atrribute1 != 'none':
        C3Atrribute2 = input("Please input Chracter 3's second attribute, enter 'none' if none: ")
    if C3Atrribute1 == 'none':
        C3Atrribute2 = 'none'
    Character3 = Character(C3Name, C3Race, C3Atrribute1, C3Atrribute2, 0, 100)
    ##Character creator##

    print(" ")
    print(Character1.characterdesc())
    print(" ")
    print(Character2.characterdesc())
    print(" ")
    print(Character3.characterdesc())
    
main()
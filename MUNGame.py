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
            charAttributes = print("Item Description:" + self.__itemDescription)
    
class Character:
    def __init__(self, characterName, characterRace = "Human", characterAttributeOne = "None", characterAttributeTwo = "None", itemCount = 0, healthBar = 100):
        self.__characterName = characterName
        self.__characterAttributeOne = characterAttributeOne
        self.__characterAttributeTwo = characterAttributeTwo
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
        return self.__characterAttributeOne
    def setAttributeOne(self, newAttributeOne):
        self.__characterAttributeOne = newAttributeOne

    def getAttributeTwo(self):
        return self.__characterAttributeTwo
    def setAttributeTwo(self, newAttributeTwo):
        self.__characterAttributeTwo = newAttributeTwo

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

    def string(self):
        print("Characters Name: " + self.__characterName)
        print("Charcter Attributes:", self.__characterAttributeOne, end= '')
        if self.__characterAttributeOne != 'None':
            print("&", self.__characterAttributeTwo)
        if self.__characterAttributeOne == 'None':
            print("")
        print("Character's Inventory: ", end = '')
        print(self.getInventory())

    def lookInventory(self):
        print(" ")
        print("Opening inventory. . .")
        print(self.__inventory)
    

#def fight():

def main():
    knifeItem = Item("Knife")
    FoodItem = Item("Sham", "A questionable can of 'meat'")
    StephCharacter = Character("Steph", "Elf")
    CindyCharacter = Character("Cindy", "Human" "Magic", "Strength", "None", 110)
    StephCharacter.string()
    CindyCharacter.string()
    StephCharacter.equipItem(knifeItem)
    StephCharacter.equipItem(FoodItem)

    StephCharacter.lookInventory()
    StephCharacter.dropItem(FoodItem)
    StephCharacter.lookInventory()
    
main()
# imports from the src file. I had it as an import *, but the imports would not work
# unless I had them very specifically like this
import src.races as races
import src.classes as classes
import src.armor as armor
import src.weapons as weapons
from src.otherData import ALIGNMENT, LANGUAGES, SKILL_LIST

# importing the helper funcions
import DnDFunctions

# I was intitally using randint for my choice, watched a youtube video about random in python
# and changed my mind to choices since I think it fits better.
from random import choice

class Character():
    ''' 
    Creates a new character using 5e D&D concepts. This class follows the SOLID principles
    Since it is single responsibility, and all the functions within the class do one thing.
    The class has a single purpose of creating a character.
    '''
    def __init__(self,_class = choice(classes.CLASSES),race = choice(races.RACES),alignment = choice(ALIGNMENT)):
        self._class = _class # NOTE: this must be instantiated as _class and not class since it errors
        self.race = race
        self.alignment = alignment
        self.size = self.race.size
        self.speed = self.race.speed
        self.languages = self.race.languages
        self.equipment = []
        self.AC = 0
        self.armor = None
        self.shield = False
        self.savingThrows = self._class.savingThrows
        self.numSpells = self._class.numSpells
        self.skillProf = []
        self.hp = 0
        self.initiative = 0

    def getAbilityStat(self):
        """ Selects ability scores by 4d6 roll and dropping lowest """
        self.abilities = {"Strength":0,"Dexterity":0,"Constitution":0,"Charisma":0,"Intelligence":0,"Wisdom":0}
        
        # use the die function to roll for the ability score
        for i in self.abilities:
            scores = DnDFunctions.rollDie(4, 6)
            scores.sort()
            scores = scores[1::]
            self.abilities[i] = sum(scores)
        
        # Once rolled, get the racial mod using D&D numbers
        for i in self.abilities:
            self.abilities[i] += self.race.abilities[i]

    def getModifiers(self):
        ''' Mods the stats based on a minus 10 mod 2 as stated in the D&D compedium '''
        self.strengthMod = (self.abilities["Strength"] - 10) // 2
        self.dexterityMod = (self.abilities["Dexterity"] - 10) // 2
        self.constitutionMod = (self.abilities["Constitution"] - 10) // 2
        self.charismaMod = (self.abilities["Charisma"] - 10) // 2
        self.intelligenceMod = (self.abilities["Intelligence"] - 10) // 2
        self.wisdomMod = (self.abilities["Wisdom"] - 10) // 2
        
        # adds the stats back to the character
        self.modsList = {
            "Strength" : self.strengthMod,
            "Dexterity" : self.dexterityMod,
            "Charisma" : self.charismaMod,
            "Constitution" : self.constitutionMod,
            "Intelligence" : self.intelligenceMod,
            "Wisdom" : self.wisdomMod
        }

    def getSkillMods(self):
        ''' 
        Gets the skill mods using proficiencies and class bonues. The skills here are from
        the D&D compedium, and this dict corresponds with the dict in otherData on which stat
        the skill draws from.
        '''

        self.skills = {
        "Acrobatics":0,
        "Animal Handling":0,
        "Arcana":0,
        "Athletics":0,
        "Deception":0,
        "History":0,
        "Insight":0,
        "Intimidation":0,
        "Investigation":0,
        "Medicine":0,
        "Nature":0,
        "Perception":0,
        "Performance":0,
        "Persuasion":0,
        "Religion":0,
        "Sleight of Hand":0,
        "Stealth":0,
        "Survival":0
        }
        for i in self.skills:
            self.skills[i] = self.modsList[SKILL_LIST[i]]
            self.skills[i] += self._class.classBonus

    def getSkillProf(self):
        ''' Generates random proficiencies for the class '''
        for i in range(self._class.skills[0]):
            x = choice(self._class.skills[1])

            while (x in self.skillProf):
                x = choice(self._class.skills[1])

            self.skillProf.append(x)

    def getAlignment(self):
        ''' Selects the alighnment for the character. Accounts for the choice baias of 1 in 6'''
        
        # Needs this if statement, or an arr pops up every 6 generations about length of NoneType
        if self.race.alignment:
            if DnDFunctions.rollDie(1,6) == 1:
                self.alignment = choice(ALIGNMENT)
            self.alignment = choice(self.race.alignment)
        else:
            self.alignment = choice(ALIGNMENT)

    def getLanguages(self):
        ''' Gets the language for the race. Some races are required to have a certain language'''
        langs = LANGUAGES
        if self.race.name == "Human":
            langs.remove("Common")
            self.languages.append(choice(langs))

        elif self.race.name == "Half-Elf":
            langs.remove("Common")
            langs.remove("Elvish")
            self.languages.append(choice(langs))

        elif self.race.name == "Dwarf":
            self.languages.remove("Dwarvish")
            self.languages.append(choice(langs))

        elif self.race.name == 'Elf':
            langs.remove("Elvish")
            self.languages.append(choice(langs))

    def getExtraInfo(self):
        ''' Calls the extra info of the hit dice points and the initiative points '''
        self.hp = self._class.hitD + self.abilities["Constitution"]
        self.initiative = self.abilities["Dexterity"]

    def equipHelper(self, style):
        ''' Recursive helper function for the equipment function. Gets what style weapon it is'''
        # gets the count of ranged weapons for the class
        if style == "Ranged":
            count = 0
            for obj in self.equipment:
                if obj in weapons.RANGED:
                    count += 1
            return count
        
        # gets the count of the armor for the class
        elif style == "Armor":
            count = 0
            for obj in self.equipment:
                if obj in armor.ARMOR:
                    count += 1
            return count

    def getEquip(self):
        ''' Gets the equipment for the character '''
        for i in self._class.equipment:
            # interates through the potential equipment list
            while True:
                selection = choice(i)
                if type(selection) is list:
                    if selection[0] not in self.equipment:
                        break
                if selection not in self.equipment:
                    break
            if type(selection) is list:
                for i in selection:
                    self.equipment.append(i)
            else:
                self.equipment.append(selection)
        
        # appends the new data to the character stats
        for i in self.equipment:
            if i == "Shield":
                self.shield = True
            for j in armor.ARMOR:
                if i == j.name:
                    self.armor = j
        
        ''' Recursion here! I wanted to try and be fancy haha! Continues calling until the
        number of equipment is full. '''
        if self.equipHelper("Ranged") > 1 or self.equipHelper("Armor") > 1:
            self.equipment = []
            self.getEquip()

    def getAC(self):
        """ Gets the armor class and the number associated with it from the three categories """
        # checks if light armor class
        if self.armor in armor.LIGHT_ARMOR:
            if self.dexterityMod > 2:
                self.AC = self.armor.AC + 2
            else:
                self.AC = self.armor.AC + self.dexterityMod

        # checks if medium armor class
        elif self.armor in armor.MEDIUM_ARMOR:
            if self.dexterityMod > 2:
                self.AC = self.armor.AC + 2
            else:
                self.AC = self.armor.AC + self.dexterityMod
        
        # checks if heavy armor class
        elif self.armor in armor.HEAVY_ARMOR:
            if self.dexterityMod > 2:
                self.AC = self.armor.AC + 2
            else:
                self.AC = self.armor.AC + self.dexterityMod

        # adds to the armor class regardless of any other item
        self.AC += 2

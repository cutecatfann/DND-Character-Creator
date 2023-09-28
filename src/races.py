from typing import List   

class Race:
    ''' Creates an instatiation of the race for the character object '''
    def __init__(self, name: str, abilities: dict, alignment: List[str], size: str, speed:int, languages: List[str]):
        self.name = name
        self.abilities = abilities
        self.alignment = alignment
        self.size = size
        self.speed = speed
        self.languages = languages

# all racial data directly from the D&D compedium. None of the data is mine, I am just using under fair use laws :)
DRAGONBORN = Race("Dragonborn",
    {
    "Strength":2,
    "Dexterity":0,
    "Constitution":0,
    "Charisma":1,
    "Intelligence":0,
    "Wisdom":0
    },
    ["Chaotic Evil", "Chaotic Good", "Lawful Evil", "Lawful Good"],"Medium",30,["Common", "Draconic"]
)
DWARF = Race("Dwarf",
    {
    "Strength":0,
    "Dexterity":0,
    "Constitution":2,
    "Charisma":0,
    "Intelligence":0,
    "Wisdom":0
    },
    None,"Medium",25,["Common", "Dwarvish"]
)
ELF = Race("Elf",
    {
    "Strength":     0,
    "Dexterity":    2,
    "Constitution": 0,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0,
    },
    ["Chaotic Good"],"Medium",30,["Common", "Elvish"]
)
GNOME = Race("Gnome",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 0,
    "Charisma":     0,
    "Intelligence": 2,
    "Wisdom":       0
    },
    ["Chaotic Good", "Neutral Good", "Lawful Good"],"Small",25,["Common", "Gnomish"]
)
HALFLING = Race("Halfling",
    {
    "Strength":     0,
    "Dexterity":    2,
    "Constitution": 0,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0
    },
    ["Lawful Good"],"Small",25,["Common", "Halfling"]
)
HALFELF = Race("Half-Elf",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 0,
    "Charisma":     2,
    "Intelligence": 0,
    "Wisdom":       0
    },
    ["Chaotic Good", "Chaotic Neutral", "Chaotic Evil"],"Medium",30,["Common", "Elvish", "Any"]
)
HALFORC = Race("Half-Orc",
    {
    "Strength":     2,
    "Dexterity":    0,
    "Constitution": 1,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0
    },
    ["Chaotic Evil"],"Medium",25,["Common", "Orc"]
)
HUMAN = Race(
    "Human",
    {
    "Strength":     1,
    "Dexterity":    1,
    "Constitution": 1,
    "Charisma":     1,
    "Intelligence": 1,
    "Wisdom":       1
    },
    None,"Medium",30,["Common", "Any"]
)
TIEFLING = Race("Tiefling",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 0,
    "Charisma":     2,
    "Intelligence": 1,
    "Wisdom":       0
    },
    ["Chaotic Good", "Chaotic Neutral", "Chaotic Evil"],"Medium",30,["Common", "Infernal"]
)

# list of race objects
RACES = [DRAGONBORN,DWARF,ELF,GNOME,HALFELF,HALFORC,HALFLING,HUMAN,TIEFLING]

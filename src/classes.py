from typing import List
class Class():
    ''' Class for creating the class information for each character '''
    def __init__(self, name: str, hitD: int, armorClass: List[str], weaponClass: List[str], tools, savingThrows, skills, equipment, features: List[str], cantrips: int, classSpells, numSpells: int):
        self.name = name
        self.hitD = hitD
        self.armorClass = armorClass
        self.weaponClass = weaponClass
        self.tools = tools
        self.savingThrows = savingThrows
        self.skills = skills
        self.equipment = equipment
        self.features = features
        self.cantrips = cantrips
        self.classSpells = classSpells
        self.numSpells = numSpells
        self.classBonus = 1

""" 
Alphabetical listing of all classes from D&D with the given stats from the source code.
All the data is not mine, is taken from the D&D 5th edition.
Each class is instantiated as a class of Class with data for 
- name of class
- hit dice points
- armor classes the class can use
- weapons classes the class can use
- the tools of the class (as outlined in the D&D compedium
- the stats that have saving throws associated with them
- the skill ponts and the skills the class can attain
- the equipment that is associated with the class
- the features of the class as outlined
- The cantrip points of the class
- the spells the class has
- the number of spell slots for the class
- the class bonus points
"""

BARBARIAN = Class("Barbarian",12,["Light Armor", "Medium Armor", "Shields"], 
    ["Simple", "Martial"],None,["Strength", "Constitution"],
    [2, ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]],
    [
        ["Greataxe", "Any Martial"],
        ["2 Handaxes", "Any Simple"],
        [["Explorer's Pack", "4 Javelins"]]
    ],
    ["Rage", "Unarmored Defense"],None,None,None
)
BARD = Class("Bard",12,["Light Armor"],
    ["Simple", "Hand Crossbow", "Longsword", "Rapier", "Shortsword"],
    "Three musical instruments",["Dexterity", "Charisma"],
    [2, ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana",
        "History", "Investigation", "Nature", "Religion", "Animal Handling",
        "Insight", "Medicine", "Perception", "Survival", "Deception",
        "Intimidation", "Performance", "Persuasion"]],
    [
        ["Rapier", "Longsword", "Any Simple"],
        ["Diplomat's Pack", "Entertainer's Pack"],
        ["Lute", "Any instrument"],
        ["Leather"],
        ["Dagger"]
    ], ["Bardic Inspo","Spellcasting"],2,4,2
)
CLERIC = Class("Cleric",8,["Light Armor", "Medium Armor", "Shields"],
    ["Simple"],None,["Wisdom", "Charisma"],
    [2, ["History", "Insight", "Medicine", "Persuasion", "Religion"]],
    [
        ["Mace"],
        ["Scale Mail", "Leather"],
        ["Light Crossbow and 20 Bolts", "Any Simple"],
        ["Priest's Pack", "Explorer's Pack"],
        ["Shield"],
        ["Holy Symbol"]
    ],["Divine Domain","Spellcasting"],3,"Wisdom mod + cleric level",2
)
DRUID = Class("Druid",8,["Light Armor", "Medium Armor", "Shields"],
    ["Club", "Dagger", "Dart", "Javelin", "Mace", "Quarterstaff", "Scimitar", "Sling", "Spear"],
    "Herbalism Kit",["Intelligence", "Wisdom"],
    [2, ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]],
    [
        ["Shield", "Any Simple"],
        ["Scimitar", "Any Simple Melee"],
        ["Leather"],
        ["Explorer's Pack"],
        ["Druidic Focus"]
    ],["Druidic", "Spellcasting"],2,"Wisdom mod + druid level",2
)
FIGHTER = Class("Fighter",10,["Light Armor", "Medium Armor", "Heavy Armor", "Shields"],
    ["Simple", "Martial"],None,["Strength", "Constitution"],
    [2, ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight",
        "Intimidation", "Perception", "Survival"]],
    [
        ["Chain Mail", ["Leather", "Longbow", "20 Arrows"]],
        [["Any Martial", "Shield"], "Any 2 Martial"],
        [["Light Crossbow", "20 Bolts"], "2 Handaxes"],
        ["Dungeoneer's Pack", "Explorer's Pack"]
    ],
    ["Fighting Style", "Second Wind"],None,None,None
)
MONK = Class("Monk",8,None,["Simple", "Shortsword"],
    ["One Artisan's Tools", "One instrument"],["Strength", "Dexterity"],
    [2, ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]],
    [
        ["Shortsword", "Any Simple"],
        ["Dungeoneer's Pack", "Explorer's Pack"],
        ["10 Darts"]
    ],
    ["Martial Arts","Unarmored Defense"],None,None,None
)
PALADIN = Class("Paladin",10,["Light Armor", "Medium Armor", "Heavy Armor", "Shields"],
    ["Simple", "Martial"],None,["Wisdom", "Charisma"],
    [2, ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]],
    [
        [["Any Martial", "Shield"], "Any 2 Martial"],
        ["5 Javelins", "Any Simple Melee"],
        ["Priest's Pack", "Explorer's Pack"],
        [["Chain Mail", "Holy Symbol"]]
    ],
    ["Divine Sense", "Lay on Hands"],None,None,None
)
RANGER = Class("Ranger",10,["Light Armor", "Medium Armor", "Shields"],
    ["Simple", "Martial"],None,["Strength", "Dexterity"],
    [3, ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]],
    [
        ["Scale Mail", "Leather"],
        ["2 Shortswords", "Any 2 Simple Melee"],
        ["Dungeoneer's Pack", "Explorer's Pack"],
        [["Longbow", "20 Arrows"]]
    ],
    ["Favored Enemy", "Explorer"],None,None,None
)
ROGUE = Class("Rogue",8,["Light Armor"],["Simple", "Hand Crossbow", "Longswords", "Rapier", "Shortsword"],
    "Thief's Tools",["Dexterity", "Intelligence"],
    [4, ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]],
    [
        ["Rapier", "Shortsword"],
        [["Shortbow", "20 Arrows"], "Shortsword"],
        ["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"],
        [["Leather", "2 Daggers", "Thieve's Tools"]]
    ],
    ["Expertise", "Sneak Attack(1d6)", "Thieves' Cant"],None,None,None
)
SORCERER = Class("Sorceror",6,None,
    ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
    None,["Constitution", "Charisma"],
    [2, ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]],
    [
        [["Light Crossbow", "20 Bolts"], "Any Simple"],
        ["Component Pouch", "Arcane Focus"],
        ["Dungeoneer's Pack", "Explorer's Pack"],
        ["2 Daggers"]
    ],
    ["Spellcasting", "Sorcerous Origin"],4,2,2
)
WARLOCK = Class("Warlock",8,["Light Armor"],["Simple"],None,["Wisdom", "Charisma"],
    [2, ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]],
    [
        [["Light Crossbow", "20 Bolts"], "Any Simple"],
        ["Component Pouch", "Arcane Focus"],
        ["Scholar's Pack", "Dungeoneer's Pack"],
        [["Leather", "Any Simple", "2 Daggers"]]
    ],
    ["Otherworldly Patron", "Pact Magic"],2, 2,1
)
WIZARD = Class("Wizard",6,None,
    ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
    None,["Intelligence", "Wisdom"],
    [2, ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]],
    [
        ["Quarterstaff", "Dagger"],
        ["Component Pouch", "Arcane Focus"],
        ["Scholar's Pack", "Explorer's Pack"],
        ["Spellbook"]
    ],
    ["Spellcasting", "Arcane Recovery"],3,"Intelligence mod + Wizard level",2
)

# list of all classes within the class object
CLASSES = [BARBARIAN,BARD,CLERIC,DRUID,FIGHTER,MONK,PALADIN,RANGER,ROGUE,SORCERER,WARLOCK,WIZARD]

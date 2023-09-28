""" List of potential alignments for character """
ALIGNMENT = [   "Chaotic Good",  "Chaotic Neutral",  "Chaotic Evil",
                "Neutral Good",  "True Neutral",     "Neutral Evil",
                "Lawful Good",   "Lawful Neutral",   "Lawful Evil"
]

""" List of languages from D&D """
LANGUAGES = ["Common","Elvish","Giant","Halfling","Dwarvish","Gnomish","Goblin","Orc"]

""" Skills associated with their stat in the below dictionary. Directly from D&D"""
SKILL_LIST = {
        # skills associated with charisma
        "Deception":"Charisma",
        "Intimidation":"Charisma",
        "Performance":"Charisma",
        "Persuasion":"Charisma",

        # skills associated with dexterity
        "Acrobatics":"Dexterity",
        "Sleight of Hand":"Dexterity",
        "Stealth":"Dexterity",

        # skills associated with intelligence
        "Arcana":"Intelligence",
        "History":"Intelligence",
        "Investigation":"Intelligence",
        "Nature":"Intelligence",
        "Religion":"Intelligence",

        # skills associated with strength
        "Athletics":"Strength",
        
        # skills associated with wisdom
        "Insight":"Wisdom",
        "Medicine":"Wisdom",
        "Perception":"Wisdom",
        "Animal Handling":"Wisdom",
        "Survival":"Wisdom"
    }

from typing import List
class Weapon:
    def __init__(self, name: str, cost, damage, damageType: str, distance, weight, properties:List[str], melee = True):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.damageType = damageType
        self.distance = distance
        self.weight = weight
        self.properties = properties
        self.melee = melee

""" 
Data for some of the 5e D&D weapons. 
There is the Melee Simple, Ranged Simple, Melee Martial, Ranged Martial categories.
This data is directley from the 5e D&D weapon category.
The Weapon class has data for 
- name of weapon
- cost of the weapon (directly from D&D)
- the damage amount for the weapon
- damage type in string of weapon
- the distance for the ranged weapons
- properties of the weapon
- if the weapon is melee (bool)

This data is sorted alphabetically and by categories from the copediumn
"""

# Simple Melee Type Weapons
CLUB = Weapon("Club",.01,(1, 4),"bludgeoning",None,2,["light"])
DAGGER = Weapon("Dagger",2,(1, 4),"piercing",[20, 60],1,["finesse", "light", "thrown"])
GREATCLUB = Weapon("Greatclub",.02,(1, 8),"bludgeoning",None,10,["two-handed"])
HANDAXE = Weapon("Handaxe",5,(1, 6),"slashing",[20, 60],2,["light", "thrown"])
JAVELIN = Weapon("Javelin",.05,(1, 6),"piercing",[30, 120],2,["thrown"])
LIGHTHAMMER = Weapon("Light_Hammer",2,(1, 4),"bludgeoning",[20, 60],2,["light", "thrown"] )
MACE = Weapon("Mace",5,(1, 6),"bludgeoning",None,4,None)
QUARTERSTAFF = Weapon("Quarterstaff",.02,(1, 6),"bludgeoning",None,4,["versatile8"])
SICKLE = Weapon("Sickle",1,(1, 4),"slashing",None,2,["light"])
SPEAR = Weapon("Spear",1,(1, 6),"piercing",[20, 60],3,["thrown", "versatile8"])

# Simple Ranged Type Weapons
LIGHTCROSSBOW = Weapon("Light Crossbow",25,(1, 8),"piercing",[80, 320],5,["ammunition", "loading", "two-handed"], melee = False)
SHORTBOW = Weapon("Shortbow",25,(1, 6),"piercing",[80, 320],2,["ammunition", "two-handed"],melee = False)
SLING = Weapon("Sling",.01,(1, 4),"bludgeoning",[30, 120],None,["ammunition"],melee = False)

# Martial Melee Type Weapons
BATTLEAXE = Weapon("Battleaxe",10,(1, 8),"slashing",None,4,["versatile10"])
GREATAXE = Weapon("Greataxe",30,(1, 12),"slashing",None,7,["heavy", "two-handed"])
GREATSWORD = Weapon("Greatsword",50,(2, 6),"slashing",None,6,["heavy", "two-handed"])
LONGSWORD = Weapon("Longsword",15,(1, 8),"slashing",None,3,["versatile10"])
MORNINGSTAR = Weapon("Morningstar",15,(1, 8),"piercing",None,4,None)
RAPIER = Weapon("Rapier",25,(1, 8),"piercing",None,2,["finesse"])
SHORTSWORD = Weapon("Shortsword",10,(1, 6),"piercing",None,2,["finesse", "light"])
WARHAMMER = Weapon("Warhammer",15,(1, 8),"bludgeoning",None,2,["versatile10"])
WHIP = Weapon("Weapon",2,(1, 4),"slashing",None,3,["finesse", "reach"])

# Marrial Ranged Type Weapons
BLOWGUN = Weapon("Blowgun",10,1,"piercing",[25, 100],1,["ammunition", "loading"],melee = False )
CROSSBOW_HEAVY = Weapon("Heavy Crossbow",50,(1, 10),"piercing",[100, 400],18,["ammunition", "heavy", "loading", "two-handed"],melee = False)
LONGBOW = Weapon("Longbow",50,(1, 8),"piercing",[150, 600],2,["ammunition", "heavy", "two-handed"],melee = False)
NET = Weapon("Net",1,None,None,[5, 15],3,["thrown", "special^2"],melee = False)

SIMPLE_MELEE = [CLUB,DAGGER,GREATCLUB,HANDAXE,JAVELIN,LIGHTHAMMER,MACE,QUARTERSTAFF,SICKLE,SPEAR]
SIMPLE_RANGED = [LIGHTCROSSBOW,SHORTBOW,SLING]
MARTIAL_MELEE = [BATTLEAXE,GREATAXE,GREATSWORD,LONGSWORD,MORNINGSTAR,RAPIER,SHORTSWORD,WARHAMMER,WHIP]
MARTIAL_RANGED = [BLOWGUN,CROSSBOW_HEAVY,LONGBOW,NET]

SIMPLE = [j for i in [SIMPLE_MELEE, SIMPLE_RANGED] for j in i]
MARTIAL = [j for i in [MARTIAL_MELEE, MARTIAL_RANGED] for j in i]
RANGED = [j for i in [SIMPLE_RANGED, MARTIAL_RANGED] for j in i]

# THIS TOOK SO MUCH TIMEE. I had to go through the entire compedium haha
# not all weapons are implemented. I just sincerely did not want to go thorugh the many many weapons available

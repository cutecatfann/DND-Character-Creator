class Armor:
    ''' Armor class for creating armor for each character '''
    def __init__(self, name: str, AC: int, strength, stealth, weight: int):
        self.name = name
        self.AC = AC
        self.strength = strength
        self.stealth = stealth
        self.weight = weight

""" 
armor data from D&D Directly
Each armor type is instantiated as a class of Armor with data for
- name of armor
- the armor class bonus
- the strength bonus from the armor
- the stealth bonus from the armor
- weight of the armor
"""

PADDED = Armor("Padded",11,None,-1,8)
LEATHER = Armor("Leather",11,None,True,10)
Studded_Leather = Armor("Studded Leather",12,None,None,13)
HIDE = Armor("Hide",12,None,None,12)
CHAIN_SHIRT = Armor("Chain Shirt",13,None,None,20)
SCALE_MAIL= Armor("Scale Mail",14,None,True,45)
BREASTPLATE = Armor("Breastplate",14,None,None,20)
HALF_PLATE = Armor("Half Plate",15,None,True,40)
RING_MAIL = Armor("Ring Mail",14,None,True,40)
CHAIN_MAIL= Armor("Chain Mail",16,13,True,55)
SPLINT_MAIL = Armor("Splint Mail",17,15,True,60)
PLATE_MAIL = Armor("Plate Mail",18,15,True,65)
SHIELD = Armor("Shield",2,None,None,6)

# list of all armor types within the Armor object
LIGHT_ARMOR = [PADDED, LEATHER, Studded_Leather]
MEDIUM_ARMOR = [HIDE, CHAIN_SHIRT, SCALE_MAIL, BREASTPLATE]
HEAVY_ARMOR = [RING_MAIL, CHAIN_MAIL, SPLINT_MAIL, PLATE_MAIL]
SHIELD = [SHIELD]
ARMOR = [j for i in [LIGHT_ARMOR, MEDIUM_ARMOR, HEAVY_ARMOR] for j in i]

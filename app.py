'''
Calls the controller from here. All interaction with the user happens here.
'''

from newCharacter import Character
from baseCharacter import BaseCharacter

print("WELCOME FRIEND \n Are you ready to test your fate and fortune?")
print("\nCreate a new character to adventure with...")
userInput = input("Enter a name: ")

# calls the functions in the Character class
char = Character()
char.getAbilityStat()
char.getAlignment()
char.getExtraInfo()
char.getLanguages()
char.getModifiers()
char.getEquip()
char.getAC()
char.getSkillProf()
char.getSkillMods()

if char == None:
    BaseCharacter.print()
else:

    print("\n")
    print(userInput)
    print(char.race.name, char._class.name)
    print(char.alignment)
    print("Abilities: ", char.abilities)
    print("Languages: ", char.languages)
    print("Equipment: ", char.equipment)
    print("Armor Class: ", char.AC)
    print("Skill Proficiencies: ", char.skillProf)
    print("Number of Spells:", char.numSpells, "\n\n")

print("Enjoy your journey, or generate a different character! ")

# DND Inspired Character Creator
**Author:** Mimi Pieper

## Credits
All data in this application is sourced from the [D&D 5th Edition Compendium](https://roll20.net/compendium/dnd5e/Magic%20Items#h-Armor). While the code is mine, stats and details for armor, classes, and races are credited to D&D 5th Edition. This use respects copyright and fair use laws. Please report any data discrepancies; not all D&D equipment types are integrated.

## Overview
This application automates D&D character creation. It generates characters complete with stats, class, race, and additional attributes in line with the D&D fifth edition manual.

**Execution:** `python3 app.py`

## Core Algorithms and Design

### Design Patterns

1. **MVC (Model-View-Controller)**
    - The user's interaction is managed by `main.py`.
    - The character creation logic acts as the controller, which in turn influences the model—consisting of race, weapon, armor, and class modules.

2. **Bridge Pattern**
    - Facilitates the interaction of varied functionalities, races, and classes, allowing them to work cohesively.

3. **Null Object Pattern**
    - Utilized in the placeholder character feature. This default character acts as a safety net for situations where the algorithm may fail or if certain data isn't available.

4. **Optimized Design**
    - Instead of incorporating flyweight design to address repetitive code, an exhaustive data file is used to consolidate necessary information.

### SOLID Principles

- **Single Responsibility (S)**: Each class or function has a distinct function. For instance, the character creator has multiple internal operations, but each is confined to its dedicated function, focusing on the sole task of generating a new character.

- **Open-Closed (O)**: The application is designed for extensibility. New content, like additional weapons, can be effortlessly incorporated with minimal alterations.

- **Interface Segregation (I)**: The code is modular, granting users the flexibility to remove or modify sections as per their requirements.

- **Dependency Inversion (D)**: Most of the data classes are abstract, emphasizing dependency on abstractions rather than concretions. This project doesn't emphasize much on inheritance, thus the full essence of this principle isn't deeply manifested.

**Contributing:**
I welcome contributions, suggestions, and feedback. Feel free to fork the repository, raise issues, or submit pull requests.

**License:**
This project is open-source. Kindly refer to the accompanying license file for more details.

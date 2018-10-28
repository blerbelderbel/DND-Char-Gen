import constants
import random

class Character():
    def __init__(self, race, _class, background, abilities, skills, alignment, size):
        self.race = race
        self._class = _class
        self.background = background
        self.abilities = abilities
        self.skills = skills
        self.alignment = alignment
        self.size = size

class Race():
    def __init__(self, name, abilities, alignment, size, speed, languages):
        self.name = name
        self.alignment = alignment
        self.abilities = {}
        self.size = size
        self.speed = speed
        self.languages = languages
        for i in abilities:
            self.abilities[i] = abilities[i]

class _Class():
    def __init__(self, hit_dice, hp_start, armor, weapons, saves, skills, equipment):
        self.hit_dice = hit_dice
        self.hp_start = hp_start
        self.armor = armor
        self.weapons = weapons
        self.saves = saves
        self.skills = skills
        self.equipment = equipment

class Weapon():
    def __init__(self, name, cost, damage, damage_type, distance, weight, properties, melee = True):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.distance = distance
        self.weight = weight
        self.properties = properties
        self.melee = melee

class Die():
    def __init__(self, count, die):
        self.count = count
        self.die = die


#Race objects
Dwarf = Race(
    "Dwarf",
    {
    "Strength":     0,
    "Dexterity":    0,
    "Constitution": 2,
    "Charisma":     0,
    "Intelligence": 0,
    "Wisdom":       0
    },
    [],
    "Medium",
    25,
    ["Common", "Dwarvish"]
)
Human = Race(
    "Human",
    {
    "Strength":     1,
    "Dexterity":    1,
    "Constitution": 1,
    "Charisma":     1,
    "Intelligence": 1,
    "Wisdom":       1
    },
    [],
    "Medium",
    30,
    ["Common", random.choice(constants.LANGUAGES)]
)

#Melee Simple
Club = Weapon(
    "Club",
    .01,
    Die(1, 4),
    "Bludgeoning",
    None,
    2,
    ["light"]
)
Dagger = Weapon(
    "Dagger",
    2,
    Die(1, 4),
    "Piercing",
    [20, 60],
    1,
    ["finesse", "light", "thrown"]
)
Greatclub = Weapon(
    "Greatclub",
    .02,
    Die(1, 8),
    "Bludgeoning",
    None,
    10,
    ["two-handed"]
)
Handaxe = Weapon(
    "Handaxe",
    5,
    Die(1, 6),
    "Slashing",
    [20, 60],
    2,
    ["light", "thrown"]
)
Javelin = Weapon(
    "Javelin",
    .05,
    Die(1, 6),
    "Piercing",
    [30, 120],
    2,
    ["thrown"]
)
Light_Hammer = Weapon(
    "Light_Hammer",
    2,
    Die(1, 4),
    "Bludgeoning",
    [20, 60],
    2,
   ["light", "thrown"] 
)
Mace = Weapon(
    "Mace",
    5,
    Die(1, 6),
    "Bludgeoning",
    None,
    4,
    None
)
Quarterstaff = Weapon(
    "Quarterstaff",
    .02,
    Die(1, 6),
    "Bludgeoning",
    None,
    4,
    ["versatile8"]
)
Sickle = Weapon(
    "Sickle",
    1,
    Die(1, 4),
    "Slashing",
    None,
    2,
    ["light"]
)
Spear = Weapon(
    "Spear",
    1,
    Die(1, 6),
    "Piercing",
    [20, 60],
    3,
    ["thrown", "versatile8"]
)
#Ranged Simple
Light_Crossbow = Weapon(
    "Light Crossbow",
    25,
    Die(1, 8),
    "Piercing",
    [80, 320],
    5,
    ["ammunition", "loading", "two-handed"],
    melee = False
)
Dart = Weapon(
    "Dart",
    .005,
    Die(1, 4),
    "Piercing",
    [20, 60],
    .25,
    ["finesse", "thrown"],
    melee = False 
)
Shortbow = Weapon(
    "Shortbow",
    25,
    Die(1, 6),
    "Piercing",
    [80, 320],
    2,
    ["ammunition", "two-handed"],
    melee = False
)
Sling = Weapon(
    "Sling",
    .01,
    Die(1, 4),
    "Bludgeoning",
    [30, 120],
    None,
    ["ammunition"],
    melee = False
)
#Melee Martial
Battleaxe = Weapon(
    "Battleaxe",
    10,
    Die(1, 8),
    "Slashing",
    None,
    4,
    ["versatile10"]
)
Flail = Weapon(
    "Flail",
    10,
    Die(1, 8),
    "Bludgeoning",
    None,
    2,
    None
)
Glaive = Weapon(
    "Glaive",
    20,
    Die(1, 10),
    "Slashing",
    None,
    6,
    ["heavy", "reach", "two-handed"]
)
Greataxe = Weapon(
    "Greataxe",
    30,
    Die(1, 12),
    "Slashing",
    None,
    7,
    ["heavy", "two-handed"]
)
Greatsword = Weapon(
    "Greatsword",
    50,
    Die(2, 6),
    "Slashing",
    None,
    6,
    ["heavy", "two-handed"]
)
Halberd = Weapon(
    "Halberd",
    20,
    Die(1, 10),
    "Slashing",
    None,
    6,
    ["heavy", "reach", "two-handed"]
)
# Lance = Weapon(
#     "Lance",
#     10,
#     Die(1, 12),
#     "Piercing",
#     None,
#     6,
#     ["reach","special^1"]
# )
Longsword = Weapon(
    "Longsword",
    15,
    Die(1, 8),
    "Slashing",
    None,
    3,
    ["versatile10"]
)
Maul = Weapon(
    "Maul",
    10,
    Die(2, 6),
    "Bludgeoning",
    None,
    10,
    ["heavy", "two-handed"]
)
Morningstar = Weapon(
    "Morningstar",
    15,
    Die(1, 8),
    "Piercing",
    None,
    4,
    None
)
Pike = Weapon(
    "Pike",
    5,
    Die(1, 10),
    "Piercing",
    None,
    18,
    ["heavy", "reach", "two-handed"]
)
Rapier = Weapon(
    "Rapier",
    25,
    Die(1, 8),
    "Piercing",
    None,
    2,
    ["finesse"]
)
Scimitar = Weapon(
    "Scimitar",
    25,
    Die(1, 6),
    "Slashing",
    None,
    3,
    ["finesse", "light"]
)
Shortsword = Weapon(
    "Shortsword",
    10,
    Die(1, 6),
    "Piercing",
    None,
    2,
    ["finesse", "light"]
)
Trident = Weapon(
    "Trident",
    5,
    Die(1, 6),
    "Piercing",
    [20, 60],
    4,
    ["thrown", "versatile8"]
)
War_Pick = Weapon(
    "War Pick",
    5,
    Die(1, 8),
    "Piercing",
    None,
    2,
    None
)
Warhammer = Weapon(
    "Warhammer",
    15,
    Die(1, 8),
    "Bludgeoning",
    None,
    2,
    ["versatile10"]
)
Whip = Weapon(
    "Weapon",
    2,
    Die(1, 4),
    "Slashing",
    None,
    3,
    ["finesse", "reach"]
)
#Ranged Martial
Blowgun = Weapon(
    "Blowgun",
    10,
    Die(1, 0),
    "Piercing",
    [25, 100],
    1,
    ["ammunition", "loading"],
    melee = False 
)
Crossbow_hand = Weapon(
    "Crossbow, hand",
    75,
    Die(1, 6),
    "Piercing",
    [30, 120],
    3,
    ["ammuntion", "light", "loading"],
    melee = False
)
Crossbow_heavy = Weapon(
    "Crossbow, heavy",
    50,
    Die(1, 10),
    "Piercing",
    [100, 400],
    18,
    ["ammunition", "heavy", "loading", "two-handed"],
    melee = False
)
Longbow = Weapon(
    "Longbow",
    50,
    Die(1, 8),
    "Piercing",
    [150, 600],
    2,
    ["ammunition", "heavy", "two-handed"],
    melee = False
)
# Net = Weapon(
#     "Net",
#     1,
#     None,
#     None,
#     [5, 15],
#     3,
#     ["thrown", "special^2"],
#     melee = False
# )
<<<<<<< HEAD
class Weapon(object):
    def __init__(self, name, cost, damage, damage_type, distance, weight, properties):
=======
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
>>>>>>> 1e51ab9360a705a339db2442a5ff77a93c798526
        self.name = name
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.distance = distance
        self.weight = weight
        self.properties = properties
<<<<<<< HEAD

class Die(object):
    def __init__(self, die, count):
=======
        self.melee = melee

class Die():
    def __init__(self, count, die):
>>>>>>> 1e51ab9360a705a339db2442a5ff77a93c798526
        self.count = count
        self.die = die


<<<<<<< HEAD

Club = Weapon("Club", .01, Die(1,4), "Bludgeoning", None, 2, ["light"])
Dagger = Weapon("Dagger", 2, Die(1,4), "Piercing", [20, 60], 1, ["finesse", "light", "thrown"])
print(Club.cost)
print(Dagger.cost)
=======
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
#Melee Martial
#Ranged Martial
>>>>>>> 1e51ab9360a705a339db2442a5ff77a93c798526

#!/usr/bin/python -u
import sys, argparse
import re
import math
import locale
import itertools
import copy
from random import shuffle

# 111 vs 188

# Hit Points: 109
# Damage: 8
# Armor: 2

class Subject:
    def __init__(self, hit_points, damage, armor):
        self.hit_points = int(hit_points)
        self.damage = int(damage)
        self.armor = int(armor)

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return self.__str__()

    def strike(self, opponent):
        calc_damage = max(self.damage - opponent.armor,1)
        opponent.hit_points -= calc_damage
        return opponent.hit_points
    def equip_self(self,equipment):
        self.damage = equipment.damage
        self.armor = equipment.armor
        return self
    hit_points = 0
    damage = 0
    armor = 0


class Item:
    def __init__(self, type=None, name='', cost=0, damage=0, armor=0):
        self.type = type
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return self.__str__()

    type = ''
    name = ''
    cost = 0
    damage = 0
    armor = 0


def make_combined_item(equipment_combination):
    combined_item = Item('Combined')
    for item in equipment_combination:
        combined_item.cost += item.cost
        combined_item.damage += item.damage
        combined_item.armor += item.armor
        combined_item.name += '+' + item.name
    return combined_item


base_boss = Subject(109, 8, 2)
base_hero = Subject(100, 0, 0)
item_types = ['Weapons', 'Armor', 'Rings']


def fill_shop(fileName):
    type = ''
    toReturn = []
    for line in filter(None, (line.rstrip() for line in open(fileName))):
        data = [x for x in re.findall('\w+', line.replace(' +', '', 1))]
        if data[0] in item_types:
            type = data[0]
        else:
            i = Item(type, data[0], data[1], data[2], data[3])
            toReturn.append(i)
    return toReturn

shop = fill_shop('input21')

only_weapons = [i for i in shop if i.type == 'Weapons']
only_armor = [i for i in shop if i.type == 'Armor']
only_rings = [i for i in shop if i.type == 'Rings']
armor_and_weapons = list(itertools.product(only_weapons, only_armor))
rings_and_weapons = list(itertools.product(only_weapons, only_rings))
armor_rings_and_weapons = list(itertools.product(only_weapons, only_armor, only_rings))
# two_rings=list(itertools.combinations(only_rings,2))
rings_rings_and_weapons = list([c for c in itertools.product(only_weapons, only_rings,only_rings) if c[1]!=c[2] ])
rings_rings_armor_and_weapons = list([c for c in itertools.product(only_weapons, only_armor, only_rings,only_rings) if c[2]!=c[3]])

equipment_combinations = list()
equipment_combinations.extend(list(itertools.product(only_weapons)))
equipment_combinations.extend(armor_and_weapons)
equipment_combinations.extend(armor_rings_and_weapons)
equipment_combinations.extend(rings_and_weapons)
equipment_combinations.extend(rings_rings_and_weapons)
equipment_combinations.extend(rings_rings_armor_and_weapons)

equipment_combinations2 = list()
for i in reversed(equipment_combinations):
    equipment_combinations2.append(make_combined_item(i))


def fight(hero, boss):
    print "hero: ",hero,"\nboss:", boss
    while (hero.hit_points > 0 and boss.hit_points > 0):
        if hero.strike(boss) > 0:
            boss.strike(hero)
    print "hit result:",hero.hit_points,boss.hit_points
    return hero.hit_points>0

equipment_for_win=list()
equipment_for_loose=list()
for index,equipment in enumerate(reversed(equipment_combinations2)):
    # if index>5:break
    hero=copy.deepcopy(base_hero).equip_self(equipment)
    boss=copy.deepcopy(base_boss)
    print "\n",index,"fight\n",
    if fight(hero, boss):
        print "HERO won:", equipment.cost, equipment.name
        equipment_for_win.append(equipment)
    else:
        equipment_for_loose.append(equipment)
        print "BOSS won", equipment.cost, equipment.name

print "++++++"
print "cheapest win:",min([i.cost for i in equipment_for_win])
print "the most expensive loose:",max([i.cost for i in equipment_for_loose])

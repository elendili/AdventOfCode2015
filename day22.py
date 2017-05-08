#!/usr/bin/python -u
import sys, argparse
import re
import math
import locale
import itertools
import copy
import random
import logging
logging.basicConfig()
from random import shuffle

# 111 vs 188

# Hit Points: 71
# Damage: 10
logger = logging.getLogger("")

class Subject(object):
    def __init__(self, hit_points, damage, armor=0, mana=0):
        self.hit_points = int(hit_points)
        self.damage = int(damage)
        self.armor = int(armor)
        self.mana = int(mana)

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return self.__str__()

    def strike(self, opponent):
        calc_damage = max(self.damage - opponent.armor,1)
        opponent.hit_points -= calc_damage
        return opponent.hit_points

    hit_points = 0
    damage = 0
    armor = 0
    mana = 0




class Spell(object):
    def __str__(self): return type(self).__name__+" "+str(vars(self))
    def __repr__(self): return self.__str__()
    def tell(self,hero):
        hero.mana -=self.manaCost
    def affect(self,hero,boss):
        return None
    effect = False
    effectTimer=0
    manaCost = 0

class NoSpell(Spell):
    manaCost = 0

class MagicMissile(Spell):
    manaCost = 53
    damage=4
    def affect(self,hero,boss):
        boss.hit_points-=self.damage


class Drain(Spell):
    manaCost = 73
    damage=2
    def affect(self,hero,boss):
        boss.hit_points-=self.damage
        hero.hit_points+=2

class Effect(Spell):
    effect = True

class Shield(Spell):
    manaCost = 113; effect = True; effectTimer = 6
    def affect(self,hero,boss):
        self.effectTimer-=1
        if self.effectTimer>=0:
            hero.armor=7
        else: hero.armor=0

class Poison(Spell):
    manaCost = 173; effect = True;    effectTimer = 6
    damage=3
    def affect(self,hero,boss):
        self.effectTimer-=1
        if self.effectTimer>=0:
            boss.hit_points-=self.damage

class Recharge(Spell):
    manaCost = 229; effect = True;    effectTimer = 5
    def affect(self,hero,boss):
        self.effectTimer-=1
        if self.effectTimer>=0:
            hero.mana+=101

# =============
predefined_spells = iter([Poison,MagicMissile])
predefined_spells = iter([Recharge,Shield,Drain,Poison,MagicMissile])

def choose_spell(hero,boss,effects):
    # return predefined_spells.next()

    if hero.mana>=Recharge.manaCost and boss.hit_points>=18 and \
                    not any(isinstance(z,Poison) for z in effects) and \
                    not any(isinstance(z,Recharge) for z in effects):
        return Recharge()
    if hero.mana>=MagicMissile.manaCost and boss.hit_points<=MagicMissile.damage and \
                    any(isinstance(z,Poison) for z in effects):
        return MagicMissile()

    all_spells=[Recharge(),Poison(),Shield(),Drain(),MagicMissile()]
    spells_list = filter(lambda x: x.manaCost<=hero.mana , all_spells)
    if spells_list:
        diff = set(spells_list).difference(effects)
        chosen = random.sample(diff,1)[0]
        return chosen
    else:
        return NoSpell()


# =============
def process_effects(effects,hero,boss):
    next_effects=set()
    for effect in effects:
        effect.affect(hero,boss)
        if effect.effectTimer>0:
            next_effects.add(effect)
    return next_effects
# =============

def fight(hero, boss):
    logger.debug("\n======= FIGHT =======")
    history=list()
    effects=set()
    i=0
    spell = None
    manaSpent=0
    while (hero.hit_points > 0 and boss.hit_points > 0 ):
        i+=1
        spell=choose_spell(hero,boss,effects)
        if type(spell) is NoSpell:
            hero.hit_points=0
            break
        history.append(spell)
        logger.debug("\n"+str(i)+" Hero turn before:\nhero: "+str(hero)+ "\nboss: "+str(boss)+"\nspell: "+str(spell)+"\neffects: "+str(effects))
        spell.tell(hero)
        manaSpent +=spell.manaCost
        effects=process_effects(effects,hero,boss)
        if spell.effect:
            effects.add(spell)
        else: spell.affect(hero,boss)
        logger.debug(str(i)+" Hero turn after:\nhero: "+str(hero)+"\nboss: "+str(boss)+"\nspell: "+str(spell)+"\neffects: "+str(effects) )

        i+=1
        logger.debug(str(i)+" Boss turn before:\nhero: "+str(hero)+ "\nboss: "+str(boss)+"\neffects: "+str(effects))
        if boss.hit_points>0:
            effects=process_effects(effects,hero,boss)
            if boss.hit_points>0:
                boss.strike(hero)
        logger.debug(str(i)+" Boss turn after:\nhero: "+str(hero)+"\nboss: "+str(boss)+"\neffects: "+str(effects))


    logger.debug("\n======\nfight result:"+str("\nWIN" if hero.hit_points>0 else "\nLOOSE")+"\nhero:"+str(hero)+"\nboss:"+str(boss)+"\nfinal effects:"+str(effects)+"\nhistory"+str(history)+"manaSpent: "+str(manaSpent))
    return hero.hit_points>0, manaSpent, history


base_boss = Subject(71, 10)
base_hero = Subject(50, 0, 0, 500)
# base_boss = Subject(14, 8)
# base_hero = Subject(10, 0, 0, 250)


boss = copy.deepcopy(base_boss)
hero = copy.deepcopy(base_hero)
logging.getLogger().setLevel(logging.INFO)
base_min_mana=1355
min_mana=base_min_mana
i=0
while (min_mana>=base_min_mana):
    i+=1
    boss = copy.deepcopy(base_boss)
    hero = copy.deepcopy(base_hero)
    win, manaSpent, history = fight(hero,boss)
    # print i,win,manaSpent,history
    if win and manaSpent<min_mana:
        min_mana=manaSpent
        print i, 'spent=', manaSpent,' ', history
        logger.info("\nWIN FIGHT: "+str(i)+' manaSpent: '+str(manaSpent)+' '+str(history)+' min_mana:'+str(min_mana) )

# WIN FIGHT: 57773 manaSpent: 1355 [Recharge {'effectTimer': 0}, MagicMissile {}, Shield {'effectTimer': 0}, Recharge {'effectTimer': 0}, Poison {'effectTimer': 0}, MagicMissile {}, Poison {'effectTimer': 0}, Poison {'effectTimer': 0}, MagicMissile {}, MagicMissile {}, MagicMissile {}] min_mana:1355

#1937 = too high
#1355 = too low
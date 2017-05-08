#!/usr/bin/python -u
import sys, argparse
import re, math
import itertools
from itertools import izip, tee

input = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1""".split('\n')

# input = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".split('\n')


class Ingredient:
    def __init__(self,name, capacity, durability, flavor, texture, calories):
        self.name=name
        self.capacity=int(capacity)
        self.durability=int(durability)
        self.flavor=int(flavor)
        self.texture=int(texture)
        self.calories=int(calories)
    def __str__(self):
        return str(vars(self))
    def __repr__(self):
        return str(vars(self))
    name=""
    capacity=0
    durability=0
    flavor=0
    texture=0
    calories=0



ingredient_list = {}
for index,line in enumerate(input):
    # if index>8:break
    name, capacity, durability, flavor, texture, calories = [z for z in re.findall('[A-Z]\w+|-?\d+', line)]
    ingredient = Ingredient(name, capacity, durability, flavor, texture, calories)
    ingredient_list[ingredient.name]= ingredient

print '\n'.join([str(z) for z in ingredient_list.items()])

properties_list = [x for x in vars(ingredient).keys() if x not in ['name']]

# recipe = {"Cinnamon":60,"Butterscotch":40}
def calculate_recipe_score(recipe, ingredient_list,calories):
    multiplied_properties=1
    for property in properties_list:
        added_property=0
        for ingredient_name,count in recipe.items():
            ingredient = ingredient_list[ingredient_name]
            added_property += getattr(ingredient,property) * count
        added_property = added_property if added_property>0 else 0
        if property=='calories':
            if added_property!=calories:
                added_property=0
            else: added_property=1
        multiplied_properties *=added_property
    return multiplied_properties

# print calculate_recipe_score(recipe,ingredient_list,500)

def generate_recipes(max):
    list = [[a,b,c,d] for a in range(1,max)
            for b in range(1,max-a+1)
            for c in range(1,max-a-b+1)
            for d in range(1,max-a-b-c+1)
            if a+b+c+d==max]

    new_list=[]
    for recipe in list:
        dicti={}
        for i,count in enumerate(recipe):
            ingr = ingredient_list.keys()[i]
            dicti[ingr] = count
        new_list.append(dicti)

    return new_list

max_score=0
for recipe in generate_recipes(100):
    score = calculate_recipe_score(recipe,ingredient_list,calories=500)
    max_score = max(max_score,score)

print max_score
# print '\n'.join([str(index) +'.' + str(x) +'  ' + str(calculate_recipe_score(x, ingredient_list)) for index, x in enumerate(generate_recipes(6))])
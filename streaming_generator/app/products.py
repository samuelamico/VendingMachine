from enum import Enum
import random

random.seed()
"""
    Drink Class has the Enum config:
    name = drink name
    value = probability weight
    The total weight is 10+20+30+40+50 = 134
    List is [33, 12, 9, 8, 7, 25, 15, 9, 5, 11]

    It returns 33 with probability 0.246 (10/150) 
    It returns 12 with probability 0.09 (20/150)
    It returns 9 with probability 0.06 (30/150)
    It returns 8 with probability 0.06 (40/150)
    It returns 7 with probability 0.05 (50/150)
    It returns 25 with probability 0.18 (50/150)
    It returns 15 with probability 0.11 (50/150)
    It returns 9 with probability 0.06 (50/150)
    It returns 5 with probability 0.03 (50/150)
    It returns 11 with probability 0.08 (50/150)
"""
class Drinks(Enum):
    COKE = random.randint(20,40)
    COKE_ZERO = random.randint(10,30)
    SPRIT = random.randint(10,20)
    FANTA_UVA = random.randint(10,12)
    FANTA_LARANJA = random.randint(10,19)
    FANTA_GUARANA = random.randint(16,28)
    PUREZA = random.randint(13,24)
    GRAPETE = random.randint(1,9)
    MINEIRINHO = random.randint(4,10) 
    CAJUINA = random.randint(10,16)
# python3
# -*- coding: utf-8 -*-
import sys
import math
#from math import gcd
from itertools import count, permutations
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint

INF = float('inf')

ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
sys.setrecursionlimit(1000000000)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def attack_count(x):
    if x == 1:
        return 1
    else:
        return 2 * attack_count(math.floor(x/2)) + 1

# main
H = ii()
print(attack_count(H))

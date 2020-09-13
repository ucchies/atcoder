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


# main
S, T = input().split()
A, B = mis()
U = input()

if U == S:
    print(str(A-1) + " " + str(B))
else:
    print(str(A) + " " + str(B-1))

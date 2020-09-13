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
n,m = mis()
alist = lmis()

alist.sort()
alist.reverse()

min = sum(alist) * float(1/(4*m))

for i in range(m):
    if alist[i] < min:
        print('No')
        exit(0)

print('Yes')

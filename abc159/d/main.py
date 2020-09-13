# python3
# -*- coding: utf-8 -*-
import sys
import math
import bisect
import numpy as np
from fractions import gcd
from itertools import count, permutations
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint

INF = float('inf')

ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
lmtx = lambda h: [list(map(int, lmis())) for _ in range(h)]
sys.setrecursionlimit(1000000000)

def comb(n, r):
    r = (n - r) if (n - r) < r else r



def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    n = ii()
    alist = lmis()

    for i in range(n):


main()

# python3


def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))

    goal = n*m
    a_sum = sum(a)

    if (goal - a_sum) <= k:
        print(max(goal - a_sum, 0))
    else:
        print(-1)


main()


coins = (1, 2, 5, 10, 20, 50, 100, 200)
amount = 150


def memoise(f):
    memo = {}

    def decorated(*args):
        if args in memo.keys():
            return memo[args]
        else:
            memo[args] = f(*args)
            return f(*args)

    return decorated


@memoise
def ways_to_make(n, coins):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if len(coins) == 0:
        return 0
    else:
        return ways_to_make(n, coins[:-1]) + ways_to_make(n-coins[-1], coins)


print ways_to_make(amount, coins)

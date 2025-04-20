from random import randrange

def min_coins(value, coins):
    #Time complexity O(value x coins_len)
    dp = [float('inf')] * (value + 1)
    dp[0] = 0
    for i in range(1, value + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[value] if dp[value] != float('inf') else -1


coins_len = 4
value = randrange(2, 20)
coins = []
while len(coins) < coins_len:
    coin = randrange(1, 11)
    if coin not in coins:
        coins.append(coin)
print(f"Coins: {coins}")
min = min_coins(value, coins)
if min != -1:
    print(f"\33[34m{min}\33[0m is the minimum number of coins to make the value \33[33m{value}\33[0m")
else:
    print(f"\33[31mNot possible to make the value {value} with this coins")
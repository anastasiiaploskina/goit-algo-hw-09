from random import randint

from measure_time import measure_time_ms


@measure_time_ms
def find_coins_greedy(coins, amount):
    change = {coin: 0 for coin in coins}

    for coin in coins:
        if amount >= coin:
            quantity = amount // coin
            change[coin] += quantity
            amount -= coin * quantity

    coins_count_ordered = {coin: change.get(coin) for coin in coins if change[coin] > 0}
    return coins_count_ordered


@measure_time_ms
def find_min_coins(coins, amount):
    min_coins_required = [0] + [float("inf")] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

    coins_count = {}

    current_amount = amount

    while current_amount > 0:
        coin = coin_used[current_amount]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_amount -= coin

    coins_count_ordered = {coin: coins_count.get(coin, 0) for coin in coins if coin in coins_count}
    return coins_count_ordered


def main():
    coins = [50, 25, 10, 5, 2, 1]

    for edge in [10, 100, 1000, 10000, 100000]:
        sum = randint(1, edge)

        print("---" * 15)
        print(f"Change to give: {sum}")
        print(f"Greedy change: {find_coins_greedy(coins, sum)}")
        print(f"Dynamic change: {find_min_coins(coins, sum)}")


if __name__ == "__main__":
    main()

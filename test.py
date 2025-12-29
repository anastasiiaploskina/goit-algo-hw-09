import time
from random import randint
from functools import wraps

# --- Допоміжний декоратор (замість імпорту) ---
def measure_time_ms(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # переводимо в мілісекунди
        # Ми можемо виводити час тут або повертати його, 
        # але для чистоти виводу просто додамо його як атрибут до функції (опціонально)
        print(f"[{func.__name__}]: {execution_time:.4f} ms") 
        return result
    return wrapper

# --- Жадібний алгоритм ---
@measure_time_ms
def find_coins_greedy(coins, amount):
    # Важливо: Жадібний алгоритм вимагає сортування за спаданням
    # Ми не сортуємо тут щоразу заради швидкодії, але пам'ятаємо про це при виклику.
    
    change = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Визначаємо, скільки таких монет влазить
            change[coin] = count
            amount -= coin * count
            
    return change

# --- Динамічне програмування ---
@measure_time_ms
def find_min_coins(coins, amount):
    # Ініціалізація масиву нескінченністю. 
    # [0] означає, що для суми 0 потрібно 0 монет.
    min_coins_required = [0] + [float("inf")] * amount
    
    # Масив для відстеження, яку монету ми додали останньою для кожної суми
    coin_used = [0] * (amount + 1)

    # Заповнюємо таблицю DP
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

    # Якщо ми не знайшли рішення (сума залишилась inf), повертаємо порожній словник
    if min_coins_required[amount] == float("inf"):
        return {}

    # Відновлення результату (Backtracking)
    coins_count = {}
    current_amount = amount

    while current_amount > 0:
        coin = coin_used[current_amount]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_amount -= coin

    # Сортуємо результат для красивого виводу (від більшого номіналу до меншого)
    # Це необов'язково для логіки, але зручно для читання
    return dict(sorted(coins_count.items(), key=lambda item: item[0], reverse=True))

def main():
    # Монети мають бути відсортовані для жадібного алгоритму
    coins = [50, 25, 10, 5, 2, 1]

    # Тестуємо на різних сумах
    for edge in [10, 100, 1000, 2000]: # Зменшив 100000, бо DP буде дуже повільним
        amount = randint(1, edge)

        print("-" * 40)
        print(f"Сума для розміну: {amount}")
        
        greedy_res = find_coins_greedy(coins, amount)
        print(f"Жадібний:   {greedy_res}")
        
        dp_res = find_min_coins(coins, amount)
        print(f"Динамічний: {dp_res}")

if __name__ == "__main__":
    main()
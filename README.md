
# **Greedy Algorithm and Dynamic Programming**

This repository contains two functions that search for a random amount of change in a range up to 10, 100, 1000, 10000, 100000 using different methods (greedy and dynamic) 

---

# **find_coins_greedy()**

Searches for a random amount of change in a range up to 10, 100, 1000, 10000, 100000 using greedy method 
* Works faster than the dynamic one
* Not accurate if the coins' nominal value is changed to 1, 6, 10

# **find_min_coins()**

Searches for a random amount of change in a range up to 10, 100, 1000, 10000, 100000, searching for the least amount of coins as change 
* Works pretty slowly; the difference gap expands as the amount of change rises
* Always finds the least amount of coins

---

## **Emaple Usage**

```
---------------------------------------------
Change to give: 9

Execution time for 'find_coins_greedy': 0.0099 ms
Greedy change: {5: 1, 2: 2}

Execution time for 'find_min_coins': 0.0208 ms
Dynamic change: {5: 1, 2: 2}
---------------------------------------------
Change to give: 27

Execution time for 'find_coins_greedy': 0.0074 ms
Greedy change: {25: 1, 2: 1}

Execution time for 'find_min_coins': 0.0210 ms
Dynamic change: {25: 1, 2: 1}
---------------------------------------------
Change to give: 297

Execution time for 'find_coins_greedy': 0.0063 ms
Greedy change: {50: 5, 25: 1, 10: 2, 2: 1}

Execution time for 'find_min_coins': 0.1260 ms
Dynamic change: {50: 5, 25: 1, 10: 2, 2: 1}
---------------------------------------------
Change to give: 3697

Execution time for 'find_coins_greedy': 0.0040 ms
Greedy change: {50: 73, 25: 1, 10: 2, 2: 1}

Execution time for 'find_min_coins': 1.8564 ms
Dynamic change: {50: 73, 25: 1, 10: 2, 2: 1}
---------------------------------------------
Change to give: 69719

Execution time for 'find_coins_greedy': 0.0051 ms
Greedy change: {50: 1394, 10: 1, 5: 1, 2: 2}

Execution time for 'find_min_coins': 31.8038 ms
Dynamic change: {50: 1394, 10: 1, 5: 1, 2: 2}
```

---

# **Dependencies**

This project uses only the Python standard library:

* `time`
* `functools`
* `random`

No external installations required.

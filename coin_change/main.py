def change(cents):
    coin_denom = [
        {"dollars": 100},
        {"quarters": 25},
        {"dimes": 10},
        {"nickels": 5},
        {"pennies": 1}
        ]

    coins = {}

    for obj in coin_denom:
        for key in obj:
            coin_val = obj[key]
            while cents > coin_val:
                if key not in coins:
                    print "key not in coins"
                    coins[key] = 1
                else:
                    coins[key] += 1
                cents -= coin_val
    print coins

change(199)
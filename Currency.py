# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semester 1
# December 21st, 2021


# stating each individual coin value and the function for all coins
def add_coins(quarters, dimes, nickels, pennies):
    quarters_value = 0.25
    dimes_value = 0.10
    nickels_value = 0.05
    pennies_value = 0.01

    # multiplying the  coins by their value and rounding to 2 decimal places
    dollar_value = round(
        (quarters * quarters_value + dimes * dimes_value + nickels * nickels_value + pennies * pennies_value), 2)
    return dollar_value


# stating dollar value
def make_change(dollar_value):
    quarters = 0.25
    penny = 0.01
    nickel = 0.05
    dime = 0.10

    # number of each coin
    q = 0
    p = 0
    n = 0
    d = 0

    # run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
    while dollar_value >= quarters:
        dollar_value = round(dollar_value - quarters, 2)
        q += 1

    # run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
    while dime <= dollar_value:
        dollar_value = round(dollar_value - dime, 2)
        d += 1

    # run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
    while dollar_value >= nickel:
        dollar_value = round(dollar_value - nickel, 2)
        n += 1

    # run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
    while dollar_value >= penny:
        dollar_value = round(dollar_value - penny, 2)
        p += 1

    # print coin amount via formula provided
    return f'quarters:{q}; dimes:{d}; nickels:{n}; pennies:{p}'


# coin tuple
def to_string(quarters, dimes, nickels, pennies):
    y = f'quarters:{quarters}; dimes:{dimes}; nickels:{nickels}; pennies:{pennies}'
    return y


# returning value
def to_string_from_tuple(coins):
    y = f'quarters:{coins[0]}; dimes:{coins[1]}; nickels:{coins[2]}; pennies:{coins[3]}'
    return y




from coffee import Coffee

espresso: Coffee = Coffee(1, 250, 0, 16, 4)
latte: Coffee = Coffee(2, 350, 75, 20, 7)
cappuccino: Coffee = Coffee(3, 200, 100, 12, 6)

COFFEE_DICT = {'1': espresso,
               '2': latte,
               '3': cappuccino}

from constants import COFFEE_DICT
from money import MoneyBalance
from coffee import Coffee


def spend_ingredients(available_ingredients: dict, ordered_coffee: Coffee):
    available_ingredients['water'] -= ordered_coffee.water
    available_ingredients['milk'] -= ordered_coffee.milk
    available_ingredients['coffee_beans'] -= ordered_coffee.coffee_beans
    available_ingredients['disposable_cups'] -= ordered_coffee.disposable_cups


def get_money(money_balance: MoneyBalance, ordered_coffee: Coffee):
    money_balance.balance += ordered_coffee.price


def check_availability(available_ingredients: dict, ordered_coffee: Coffee):
    ordered_coffee_dict = ordered_coffee.__dict__
    for ingredient in available_ingredients.keys():
        if available_ingredients[ingredient] < ordered_coffee_dict[ingredient]:
            print(f'Sorry, not enough {ingredient}!\n')
            return False
    return True


def execute_buy(available_ingredients: dict, money_balance: MoneyBalance):
    coffee_kind_number: str = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
    if coffee_kind_number == 'back':
        return
    ordered_coffee: Coffee = COFFEE_DICT[coffee_kind_number]
    if check_availability(available_ingredients, ordered_coffee):
        spend_ingredients(available_ingredients, ordered_coffee)
        get_money(money_balance, ordered_coffee)
        print('I have enough resources, making you a coffee!\n')


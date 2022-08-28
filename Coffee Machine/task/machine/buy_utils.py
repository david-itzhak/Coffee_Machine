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


def execute_buy(available_ingredients: dict, money_balance: MoneyBalance):
    coffee_kind_number: str = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
    ordered_coffee: Coffee = COFFEE_DICT[coffee_kind_number]
    spend_ingredients(available_ingredients, ordered_coffee)
    get_money(money_balance, ordered_coffee)

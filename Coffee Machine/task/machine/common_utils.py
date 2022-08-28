from money import MoneyBalance


def print_state(available_ingredients, money):
    print(f'''The coffee machine has:
{available_ingredients['water']} ml of water
{available_ingredients['milk']} ml of milk
{available_ingredients['coffee_beans']} g of coffee beans
{available_ingredients['disposable_cups']} disposable cups
${money.balance} of money\n''')


def get_action():
    return input('Write action (buy, fill, take):\n')


def set_start_state() -> (MoneyBalance, dict):
    money_balance: MoneyBalance = MoneyBalance(550)
    available_ingredients: dict = {'water': 400,
                                   'milk': 540,
                                   'coffee_beans': 120,
                                   'disposable_cups': 9}
    return money_balance, available_ingredients

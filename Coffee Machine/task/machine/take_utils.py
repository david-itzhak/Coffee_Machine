from money import MoneyBalance


def execute_take(money_balance: MoneyBalance):
    print(f'I gave you ${money_balance.balance}\n')
    money_balance.balance = 0
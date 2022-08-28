from buy_utils import execute_buy
from fill_utils import execute_fill
from take_utils import execute_take
from common_utils import print_state, get_action, set_start_state


def main():
    money_balance, available_ingredients = set_start_state()
    while True:
        action: str = get_action()
        if action == 'remaining':
            print_state(available_ingredients, money_balance)
        if action == 'buy':
            execute_buy(available_ingredients, money_balance)
        if action == 'fill':
            execute_fill(available_ingredients)
        if action == 'take':
            execute_take(money_balance)
        if action == 'exit':
            break


if __name__ == '__main__':
    main()

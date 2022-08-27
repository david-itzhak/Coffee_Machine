def calculate_possible_cups(ingredients_per_cup: dict, available_ingredients: dict):
    return min(map(lambda ingredient: available_ingredients[ingredient] // ingredients_per_cup[ingredient],
                   ingredients_per_cup))


def main():
    ingredients_per_cup: dict = {
        'espresso': {
            'water': 250,
            'milk': 0,
            'coffee_beans': 16,
            'disposable_cups': 1
        },
        'latte': {
            'water': 350,
            'milk': 75,
            'coffee_beans': 20,
            'disposable_cups': 1
        },
        'cappuccino': {
            'water': 200,
            'milk': 100,
            'coffee_beans': 12,
            'disposable_cups': 1
        }
    }
    price: dict = {
        'espresso': 4,
        'latte': 7,
        'cappuccino': 6
    }

    money: int = 550
    available_ingredients: dict = {'water': 400,
                                   'milk': 540,
                                   'coffee_beans': 120,
                                   'disposable_cups': 9
                                   }
    
    coffee_cups_number: int = int(input('Write how many cups of coffee you will need:\n'))
    possible_cups: int = calculate_possible_cups(ingredients_per_cup, available_ingredients)
    if coffee_cups_number == possible_cups:
        print('Yes, I can make that amount of coffee')
    elif coffee_cups_number > possible_cups:
        print(f'No, I can make only {possible_cups} cups of coffee')
    else:
        print(f'Yes, I can make that amount of coffee (and even {possible_cups - coffee_cups_number} more than that)')


if __name__ == '__main__':
    main()

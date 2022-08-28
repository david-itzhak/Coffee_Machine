def execute_fill(available_ingredients):
    available_ingredients['water'] += int(input('Write how many ml of water you want to add:\n'))
    available_ingredients['milk'] += int(input('Write how many ml of milk you want to add:\n'))
    available_ingredients['coffee_beans'] += int(input('Write how many grams of coffee beans you want to add:\n'))
    available_ingredients['disposable_cups'] += int(input('Write how many disposable cups you want to add:\n'))
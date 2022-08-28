class Coffee:
    def __init__(self, coffee_id: int, water: int, milk: int, coffee_beans: int, price: int):
        self.coffee_id: int = coffee_id
        self.water: int = water
        self.milk: int = milk
        self.coffee_beans: int = coffee_beans
        self.disposable_cups: int = 1
        self.price: int = price

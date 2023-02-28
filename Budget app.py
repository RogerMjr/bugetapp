class Catogery:
    def __init__(self, name):
        self.name = name
        self.total = 0.0
        self.ledger = []


    def __repr__(self):
        s = f"{self.name:*^30}\n"
        acc = 0

        for item in self.ledger:
            s += f"{item['description']}{item['amount']:>{30 - len(item['description'])}}\n"
            acc += item["amount"]

        s += f"total:123"
        return s


    def deposit(self, amount, *args):
        description = args[0] if args else ""

        self.total += amount
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, *args):
        can_withdraw = self.check_funds(amount)

        description = args[0] if args else ""

        if can_withdraw:
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": description})

        return can_withdraw


    def get_balance(self):
        return self.total


    def transfer(self, amount, instance):
        can_transfer = self.check_funds(amount)

        if can_transfer:
            self.withdraw(amount, f"Transfer to {instance.name}")
            self.deposit(amount, f"Transfer to {self.name}")
            return True

        return False

    def check_funds(self, amount):
        if amount > self.total:
            return False
        return True




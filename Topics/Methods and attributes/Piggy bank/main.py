class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.cents += deposit_cents
        # cents deposit done
        if self.cents > 99:
            self.dollars += int(self.cents / 100)
            self.cents = self.cents % 100
        self.dollars += deposit_dollars

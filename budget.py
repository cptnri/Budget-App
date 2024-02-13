class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = list()
        self.balance = 0.0
        self.withdraws = 0
    
    def __repr__(self):
        title = self.category.center(30, '*') + '\n'
        for prods in self.ledger:
            rows = f"{prods['description'][:23]:23}{prods['amount']:7.2f}"
            title += rows + '\n'
        title += "Total: " + str(self.balance)
        return title
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": float(-amount), "description": description})
            self.withdraws += amount
            self.balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, newcat):
        if self.withdraw(amount, "Transfer to {}".format(newcat.category)):
            newcat.deposit(amount, "Transfer from {}".format(self.category))
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
            



def create_spend_chart(categories):
    expenses = list()
    ctgr = list()
    chart = "Percentage spent by category\n"
    max_len = 0
    count = 0
    
    for cats in categories:
        expenses.append(round(cats.withdraws, 2))
        ctgr.append(cats.category)
        if len(cats.category) > max_len:
            max_len = len(cats.category)
        count += 1
        
    total = round(sum(expenses), 2)
    percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), expenses))
    
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    
    chart += '    ' + ('-' * (count * 3 + 1)) + '\n'
    
    for i in range(max_len):
        chart += ' ' * 4
        for k in ctgr:
            name = 1
            if i < len(k):
                chart += ' ' + k[i] + ' '
            else:
                chart += " " * 3  
        chart += " \n"     
    return chart.rstrip("\n") 

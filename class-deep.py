class Account():
    # state
    description = "The class makes bank accounts"
    
    #constructor
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount
        
    #method
    def get_balance(self):
        print(f"the owner {self.owner} has {self.amount} usd")
        
    def deposit(self, amount):
        print("deposit:", amount)
        self.amount += amount
        
    def withdraw(self, amount):
        print("withdraw:", amount)
        self.amount -= amount
        
        
my_account = Account("Shawn", 100)
my_account.get_balance()


print("-------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()                   
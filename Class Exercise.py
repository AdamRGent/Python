class Budget: 
 
 def __init__ (self, input_category, input_balance=0): 
    self.category = input_category
    self.balance = input_balance

 def withdraw (self, amount): 
    self.balance -= int (amount)
  
 def deposit (self, amount):
    self.balance += int (amount)

budgetobjectfood = Budget ("food")
budgetobjectclothes = Budget("clothes")
budgetobjectentertainment = Budget("entertainment")

budgetobjectfood.deposit(150)
print(budgetobjectfood.balance)

budgetobjectfood.deposit(200)
print(budgetobjectfood.balance)

budgetobjectfood.withdraw(20)
print(budgetobjectfood.balance)



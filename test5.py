class ammmm:
    def __init__(self, balance=0):
        self.balance = balance
    def ami(self, amount):
        self.balance += amount 
    def amii(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств!")       
     
acc = ammmm(2000)
print("Начальный баланс:", acc.balance)

acc.ami(50)
print("Баланс после пополнения:", acc.balance)

print("Пробуем снять 200:")
acc.amii(2000) 

acc.amii(70)
print("Баланс после успешного снятия:", acc.balance)


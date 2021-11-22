#i choose dictionary to store the instances because it can be access by key, thus, it is easy to point to the right instance to do transaction
#not implementing error handling and account balance limit, there would be negative balance

import uuid

class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{self.name}'s account. Deposited {amount}. Balance: {self.balance}"

    def withdraw(self, amount):
        self.balance -= amount
        return f"{self.name}'s account. Withdrawn {amount}. Balance: {self.balance}"

    def __str__(self):
        return f"ID: {self.id}. {self.name}'s account. Balance: {self.balance}"

class DevAccount(Account):
    def __init__(self, id, name, balance):
        super().__init__(id, name, balance)

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def transfer(self, amount, target_acc):
        self.balance -= amount
        target_acc.deposit(amount)
        return f"{self.name}'s account. Transferred {amount} to {target_acc.name}. Balance: {self.balance}"

def create_acc():
    print("\nHow many account you want to create?")
    numOfAcc = int(input())

    for x in range(numOfAcc):
        id = uuid.uuid4()
        print("\nPlease insert name for acc"+str(x+1)+":")
        name = str(input())
        print("Please insert balance for acc"+str(x+1)+":")
        balance = float(input())    
        new_acc = Account(id, name, balance)
        print("Created", new_acc, "\n")
        created_accs[id] = new_acc

created_accs = {}

print("Dev or public? (d/p)")
check_dev = str(input())
if(check_dev == "d"):
    acc1 = Account("test1", "asyraf", 5000)
    acc2 = DevAccount("test2", "ash", 10000)
    print(acc1)
    print(acc2)
    print("Acc2 balance " + str(acc2.get_balance()))
    acc2.set_balance(7500)
    print("Acc2 balance " + str(acc2.get_balance())+ " after set balance")
    print(acc2.transfer(3299, acc1))
    print(str(acc1)+ " after transferred")
else:
    while True:
        print("\nWhat you want to do, create a new acc or action with existing acc? (n/e)")
        action = str(input())
        if action == "n":
            create_acc()
        elif action == "e":
            print("\nPlease input your acc ID:")
            id = uuid.UUID(input())
            exist_acc = created_accs[id]
            loop = True
            while loop:
                print("\nWhat do you want to do, deposit, withdraw or balance? (d/w/b)")
                action = str(input())
                if action == "d":
                    print("Input your deposit amount:")
                    amount = float(input())
                    print(exist_acc.deposit(amount))
                elif action == "w":
                    print("Input your withdraw amount:")
                    amount = float(input())
                    print(exist_acc.withdraw(amount))
                elif action == "b":
                    print(exist_acc, "\n")
                else:
                    print("Invalid choice")
                
                print("\nContinue action? y/n")
                cont = str(input())
                if cont == "y":
                    loop = True
                else:
                    loop = False

        else:
            print("Invalid choice")
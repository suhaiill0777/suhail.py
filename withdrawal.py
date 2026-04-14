balance = 10000  
amount = float(input("Enter amount to withdraw: "))
if amount <= 0:
    print("Invalid amount!")
elif amount > balance:
    print("Insufficient balance!")
else:
    balance -= amount
    print("Withdrawal successful!")
    print("Remaining balance:", balance)
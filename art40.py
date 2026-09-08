balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= balance and balance - amount >= 500:
    print("Withdrawal approved")
    print("Remaining balance =", balance - amount)
else:
    print("Withdrawal rejected")
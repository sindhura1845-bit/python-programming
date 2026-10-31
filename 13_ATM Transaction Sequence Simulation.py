balance = 5000
transactions = []

for i in range(3):
    amount = int(input("Enter withdrawal amount: "))

    if amount > 0 and amount <= balance:
        balance -= amount
        transactions.append(amount)
        print("Withdrawal successful")
    else:
        print("Invalid transaction")

print("Transactions:", transactions)
print("Remaining Balance:", balance)
transactions = (1000, 2000, 1000, 3000)

print("Transactions:", transactions)

for i in range(len(transactions)):
    for j in range(i + 1, len(transactions)):
        if transactions[i] == transactions[j]:
            print("Duplicate:", transactions[i])
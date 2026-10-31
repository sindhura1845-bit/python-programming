units = [100, 250, 150, 300]
bills = []

for u in units:
    if u <= 100:
        bill = u * 2
    elif u <= 200:
        bill = 200 + (u - 100) * 3
    else:
        bill = 500 + (u - 200) * 5

    bills.append(bill)

print("Apartment Bills:", bills)
print("Highest Bill:", max(bills))
print("Highest Bill Apartment:", bills.index(max(bills)) + 1)
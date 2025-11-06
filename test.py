paraula = input("introdueix una paraula")
i = 0
for a in paraula:
    if a == ("a" or "e") or ("i" or ("o" or "u")):
        i = i+1

print(f"en {paraula} hi han {i} vocals")
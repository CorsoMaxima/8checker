asd = []

for i in range(10000):
    if "8" in str(i)[0]:
        asd.append(i)

print(asd)
print(f"There are {len(asd)} numbers out there that starts with 8.")
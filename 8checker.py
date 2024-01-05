engedélyezettszámok = []
kezdőérték = input("Mennyi legyen a kezdőérték?\nWhat should be the starting number? ")
végérték = input("Mennyi legyen a végérték?\nWhat should be the ending number? ")

try:
    kezdőérték = int(kezdőérték)
    végérték = int(végérték)

    for i in range(kezdőérték, végérték+1):
        if "8" in str(i)[0]:
            engedélyezettszámok.append(i)

    print(engedélyezettszámok)
    print(f"There are {len(engedélyezettszámok)} numbers out there that starts with 8.")

except ValueError:
    exit()

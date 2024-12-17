def Dollars():

    while True:
        try:
            # Prompt the user for a floated number
            d = float(input("$:"))

            if not float(d):
                raise ValueError("Value can not be floated")

        except ValueError as e:
            print(e)
            continue

        # Ensure the input is a positive number
        if d > 0:
            return d*100

def main():

    #  Amount of Dollars to exchange
    cents = Dollars()
    coin = []

    # Constants
    Quarters, Dimes, Nickels, Pennies = 25.0, 10.0, 5.0, 1.0
    index = 0

    while True:

        index += 1

        if cents >= Quarters:
            coin.append(Exchange(cents, Quarters)) 
            cents -= Quarters * coin[len(coin)-1]

        elif cents >= Dimes and cents < Quarters:
            coin.append(Exchange(cents, Dimes))
            cents -= Dimes * coin[len(coin)-1]

        elif cents >= Nickels and cents < Dimes:
            coin.append(Exchange(cents, Nickels))
            cents -= Nickels * coin[len(coin)-1]

        elif cents >= Pennies and cents < Nickels:
            coin.append(Exchange(cents, Pennies))
            cents -= Pennies * coin[len(coin)-1]

        else : break

    for i in coin:
        cents += i

    print(f"Total coins : {int(cents)}")

def Exchange(cents, n, coin = 0): return coin if cents < n else Exchange(cents-n, n, coin+1)

if __name__ == "__main__":
    main()

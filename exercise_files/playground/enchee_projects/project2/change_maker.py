print("""
Welcome to the vending machine change maker program
Change maker initialized.
Stock contains:
   25 nickels
   25 dimes
   25 quarters
   0 ones
   0 fives
""")

stock = {"n": 25,
         "d": 25,
         "q": 25,
         "o": 0,
         "f": 0
         }

price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
while price != 'q':
    digits = "0123456789."
    count = 0
    for i in price:
        if i in digits:
            count += 1

    if len(price) > count or price == '.':
        print("Invalid purchase price. Try again")
        print()
        price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    else:
        price_cents = int(float(price) * 100)
        if (price_cents < 0 or price_cents % 5 != 0):
            print('Illegal price: Must be a non-negative multiple of 5 cents.')
            print()
            price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
        else:
            print("""
Menu for deposits:
  'n' - deposit a nickel
  'd' - deposit a dime
  'q' - deposit a quarter
  'o' - deposit a one dollar bill
  'f' - deposit a five dollar bill
  'c' - cancel the purchase        
            """)

            total_deposit_cents = 0
            while (total_deposit_cents < price_cents):
                dollars = (price_cents - total_deposit_cents) // 100
                cents = (price_cents - total_deposit_cents) % 100
                dollars_str = '' if dollars == 0 else f"{dollars} dollars"
                cents_str = f"{cents} cents"
                if dollars_str == '':
                    due = cents_str
                else:
                    due = dollars_str + " and " + cents_str

                print(f"Payment due: {due}")
                deposit = input("Indicate your deposit: ")
                while (deposit not in ['n', 'd', 'q', 'o', 'f', 'c']):
                    print(f"Illegal selection: {deposit}")
                    deposit = input("Indicate your deposit: ")

                if (deposit == 'c'):
                    price_cents = 0
                    break

                if (deposit == 'o'):
                    total_deposit_cents += 100
                elif (deposit == 'n'):
                    total_deposit_cents += 5
                elif (deposit == 'd'):
                    total_deposit_cents += 10
                elif (deposit == 'q'):
                    total_deposit_cents += 25
                elif (deposit == 'f'):
                    total_deposit_cents += 500

                stock[deposit] += 1

            change = total_deposit_cents - price_cents

            print()
            print("Please take the change below.")
            if change == 0:
                print("  No change due.")
            else:
                q = min(change // 25, stock['q'])
                stock['q'] -= q
                d = min((change - q * 25) // 10, stock['d'])
                stock['d'] -= d
                n = min((change - q * 25 - d * 10) // 5, stock['n'])
                stock['n'] -= n

                if (q != 0):
                    print(f"   {q} quarters")
                if (d != 0):
                    print(f"   {d} dimes")
                if (n != 0):
                    print(f"   {n} nickels")
                if change > q * 25 + d * 10 + n * 5:
                    dollars = (total_deposit_cents - price_cents - q * 25 - d * 10 - n * 5) // 100
                    cents = (total_deposit_cents - price_cents - q * 25 - d * 10 - n * 5) % 100
                    dollars_str = '' if dollars == 0 else f"{dollars} dollars"
                    cents_str = f"{cents} cents"
                    if dollars_str == '':
                        due = cents_str
                    else:
                        due = dollars_str + " and " + cents_str

                    print("Machine is out of change.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is: {due}")

            print()

            print("Stock contains:")
            print(f"   {stock['n']} nickels")
            print(f"   {stock['d']} dimes")
            print(f"   {stock['q']} quarters")
            print(f"   {stock['o']} ones")
            print(f"   {stock['f']} fives")

            print()
            price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

total_cents = (stock['f']*5 + stock['o']) * 100 + stock['q'] * 25 + stock['d'] * 10 + stock['n'] * 5
dollars = total_cents // 100
cents = total_cents % 100
print(f"Total: {dollars} dollars and {cents} cents")






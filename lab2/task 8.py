exchange_rates = {"USD": 1.0, "EUR": 0.93, "PKR": 300.0, "INR": 83.0, "CNY": 7.3}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount

def main():
    print("This is a currency converter")
    print("It can conver currencies in USD, EUR, PKR, INR, CNY")

    from_currency = input("Which currency do you want to convert from: ").upper()
    if from_currency not in exchange_rates:
        print("Invalid currency. Try again.")
        return
    
    try:
        amount = float(input(f"Enter the amount in {from_currency} you want to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    
    to_currency = input("Which currency do you want to convert to: ").upper()
    if to_currency not in exchange_rates:
        print("Invalid currency. Try again.")
        return
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    
    print(amount, from_currency, "is equal to", converted_amount, to_currency)

if __name__ == "__main__":
    main()


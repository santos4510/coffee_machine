import coffee_resources

def payment(cost):
    total = 0
    while True:
        moneda = input("Insert a coin (or 'q' to exit): ")
        
        if moneda.lower() == 'q':
            break
        
        try:
            value_coin = float(moneda)
            total += value_coin
            if total < cost:
                rest = cost - total
                print(f"Cumulative total: {total} and {rest} are left")
            else:
                coffee_resources.resources['money'] += total
                break
            
        except ValueError:
            print("Please enter a valid numerical value.")

    return True
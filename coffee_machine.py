from art import cup_of_coffee
import coffe_menu 
import coffee_resources
import time
import display
import loading
import order
import resources_sufficient
import count

def coffee_machine():
    print(cup_of_coffee)
    display.display_commands()
    user_input = input("What would you like?\n")
    validate_choise(user_input)

def validate_choise(user_input):
    validatePayment = False
    while True:
        if user_input == "off":
            print("Turning off the Coffee Machine...")
            break
        elif user_input == "report":
            print("Current resource values:")
            print(f"Water: {coffee_resources.resources['water']}ml")
            print(f"Milk: {coffee_resources.resources['milk']}ml")
            print(f"Coffee: {coffee_resources.resources['coffee']}g")
            print(f"Money: €{coffee_resources.resources['money']}")
            coffee_machine()
            
        elif resources_sufficient.resourceSufficient(coffe_menu.MENU[user_input]["ingredients"]):
                print(coffe_menu.MENU[user_input]['cost'])
                validatePayment = count.payment(coffe_menu.MENU[user_input]['cost'])
                if validatePayment:
                    print(f"Preparing your {user_input.capitalize()}...")
                    loading.loading_animation(3)
                    order.process_order(user_input)
                    coffee_machine()
                else:
                    break
                    
        
        else:
            print("Invalid command. Please enter 'off' to turn off the Coffee Machine or 'report' to print the report.")
            
coffee_machine()
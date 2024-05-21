import coffe_menu
import coffee_resources

def process_order(drink):
    """Deduct the required ingredients from the resources."""
    for item in coffe_menu.MENU[drink]["ingredients"]:
        coffee_resources.resources[item] -= coffe_menu.MENU[drink]["ingredients"][item]
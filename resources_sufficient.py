import coffee_resources

def resourceSufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > coffee_resources.resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
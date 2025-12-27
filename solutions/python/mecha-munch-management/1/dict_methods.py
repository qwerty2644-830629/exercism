"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    # current_cart : dict - the shopping cart (購物車)
    # items_to_add : list adding items (要加入的物品)

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart

def read_notes(notes):

    return dict.fromkeys(notes, 1)

def update_recipes(ideas, recipe_updates):
    # ideas : old recipes (舊食譜)
    # recipe_updates : need to update recipe (要更新的食譜)
    for recipe in recipe_updates:
        ideas[recipe[0]] = recipe[1]

    return ideas

def sort_entries(cart):
    
    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    # cart : custom's item (顧客物品) 
    # aisle_mapping : item's internation (物品資訊)
    cart = dict(sorted(cart.items(), reverse = True)) # reverse cart (cart 倒序)
    new_dict = {}
    
    for item, number in cart.items():
        aisle_list = aisle_mapping[item]
        new_dict[item] = [number, aisle_list[0], aisle_list[1] ]

    return new_dict
    
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    pass

def update_store_inventory(fulfillment_cart, store_inventory):
    # fulfillment_cart : custom's item (顧客東西)
    #　store_inventory : item inventory (商品庫存)

    for item in fulfillment_cart:
        if fulfillment_cart[item][0] >= store_inventory[item][0]:
            store_inventory[item][0] = 'Out of Stock'
        else:
            store_inventory[item][0] -= fulfillment_cart[item][0]

    return store_inventory
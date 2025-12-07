"""Functions to keep track and alter inventory."""


def create_inventory(items):
    # items : list of item (物品清單)
    items_dict = {} # list of items' num (物品數量清單)
    
    for item in items:
        # add one item into dict
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1

    return items_dict

def add_items(inventory, items):
    # inventory : dict of now (庫存清單)
    # items : item need to add (要新增的物品)
    items_dict = create_inventory(items) # item turn into dict (物品清單)

    for item, number in items_dict.items() :
        # add item into inventory (物品加入庫存)
        if item in inventory:
            inventory[item] = inventory[item] + number
        else:
            inventory[item] = number

    return inventory

def decrement_items(inventory, items):
    # inventory : the dict now (庫存清單)
    # items : the item need to remove (要拿出的物品)
    
    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1

    return inventory

def remove_item(inventory, item):
    # inventory : the dict now (庫存清單)
    # item : the item need to remove from inventory (要移除的物品)

    if item in inventory:
        inventory.pop(item)

    return inventory

def list_inventory(inventory):
    # inventory  the dict now (庫存清單)
    items = sorted(list(inventory.keys())) # the items type of inventory (庫存物品清單)
    items_list = []
    
    for item in items:
        if inventory[item] != 0:
            items_list.append((item, inventory[item]))
            
    return items_list
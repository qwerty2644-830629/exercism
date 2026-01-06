def flatten(nested_list):
    items = []
    
    for item in nested_list:
        if isinstance(item, list):
            items.extend(flatten(item))
        elif item is not None:
            items.append(item)
            
    return items
inventory = {
    'croissant': 19,
    'bagel': 4,
    'muffin': 8,
    'cake': 1
}

stock_list = inventory.copy()
stock_list.update({'cookie': 1})
stock_list.pop('cake')

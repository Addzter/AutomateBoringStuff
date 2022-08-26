

inventory = {
'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12
}


# Takes a dictionary, iterates through each key-value pair
# and displays in a user-friendly way
def display_inventory(invy):
    print('Inventory:')
    item_total = 0
    for key, value in invy.items():
        print(str(value), key)
        item_total = item_total + value
    print(f'Total number of items: {item_total}')


display_inventory(inventory)

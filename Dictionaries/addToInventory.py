
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


# Adds to inventory a LIST of items
def addToInventory(inventory, addedItems):
    for item in addedItems:  # iterate over each item in loot list
        if item in inventory.keys():  # for items already in the dict/inventory
            inventory[item] = inventory[item] + 1  # add 1 to the current value
            print(f'Added 1 {item}')
        elif item not in inventory.keys():  # if it's a new item to inventory
            inventory[item] = 1  # create new key-value pair with value 1
            print(f'Added 1 {item}')


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)

display_inventory(inv)

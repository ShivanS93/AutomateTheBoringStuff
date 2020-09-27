# !python3

# fantasyGameInventory.py - Organise in game inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print("{} {}".format(k,v)) #FILL THIS PART IN
    print("Total number of items: " + str(item_total))

# displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory

def main():

    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    inv = addToInventory(inv, dragonLoot)

    displayInventory(inv)

if __name__ == '__main__':
    main()
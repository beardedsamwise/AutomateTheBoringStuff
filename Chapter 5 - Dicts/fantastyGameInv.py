def displayInventory(inventory):
    # This function takes a dictionary as an input and prints an inventory of each item
    # as well as a total number of items in inventory 
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " +  str(k))
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    # This function takes a dictionary and list as an input (in that order)
    # and adds the new loot to the current inventory of our hero
    # then calls the displayInventory function to display the items
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    displayInventory(inventory)

# New loot!
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Existing loot
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)
addToInventory(stuff, dragonLoot)
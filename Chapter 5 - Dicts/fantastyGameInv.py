def displayInventory(inventory):
    # This function takes a dictionary as an input and prints an inventory of each item
    # as well as a total number of items in inventory 
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " +  str(k))
    print("Total number of items: " + str(item_total))

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)

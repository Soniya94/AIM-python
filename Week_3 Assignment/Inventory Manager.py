 # Inventory dictionary containing product names and stock quantities
inventory = {
    "Widget": 10,
    "Gadget": 5,
    "Sensor": 0,
    "Cable": 15
}
 
# Order queue containing item names and requested quantities
orders = [
    ["Widget", 3],
    ["Sensor", 2],
    ["Gadget", 7],
    ["Cable", 10],
    ["Monitor", 2]
]
 
# List to store orders that could not be completely fulfilled
unfulfilled_orders = []
 
# Counter for completely fulfilled orders
fully_fulfilled = 0
 
# Process each order
for order in orders:
    item = order[0]
    requested = order[1]
 
    # Look up the item's stock
    stock = inventory.get(item)
 
    # Out of stock or invalid item
    if stock is None or stock == 0:
        print(f"Out of stock or missing item: {item}")
        unfulfilled_orders.append([item, requested])
 
    # Full fulfillment
    elif stock >= requested:
        inventory[item] = stock - requested
        fully_fulfilled += 1
        print(f"Order fulfilled: {item} - {requested} units")
 
    # Partial fulfillment
    elif stock > 0 and stock < requested:
        unfulfilled = requested - stock
 
        print(f"Partial fulfillment: {item} - {stock} units supplied")
        print(f"Unfulfilled: {unfulfilled} units")
 
        unfulfilled_orders.append([item, unfulfilled])
        inventory[item] = 0
 
# Final summary
print("\nFinal Inventory:")
print(inventory)
 
print("\nTotal Fully Fulfilled Orders:")
print(fully_fulfilled)
 
print("\nItems/Quantities Not Fully Supplied:")
print(unfulfilled_orders)
 
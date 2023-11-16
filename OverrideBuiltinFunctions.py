class Shopping:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return ', '.join(self.items)

    def __len__(self):
        return 2 * len(self.items)  # Custom implementation: twice the length

# Create a shopping cart
cart = Shopping()

# Add items to the cart
cart.add_item("Product A")
cart.add_item("Product B")
cart.add_item("Product C")

# Use the custom __len__ method
print("Shopping Cart Contents:", str(cart))
print("Number of Items in Cart (Twice the Length):", len(cart))
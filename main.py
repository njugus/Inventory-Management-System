class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True
        return False

    def update_quantity(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                return True
        return False

    def display_inventory(self):
        for product in self.products:
            print(product)


class InventoryManagementSystem:
    def __init__(self):
        self.inventory = Inventory()

    def add_product(self, product_id, name, price, quantity):
        product = Product(product_id, name, price, quantity)
        self.inventory.add_product(product)

    def remove_product(self, product_id):
        return self.inventory.remove_product(product_id)

    def update_quantity(self, product_id, new_quantity):
        return self.inventory.update_quantity(product_id, new_quantity)

    def display_inventory(self):
        print("Current Inventory:")
        self.inventory.display_inventory()


# Example usage:
if __name__ == "__main__":
    # Creating inventory management system
    inventory_system = InventoryManagementSystem()

    # Adding products
    inventory_system.add_product(1, "Product A", 10.99, 100)
    inventory_system.add_product(2, "Product B", 5.99, 50)

    # Displaying inventory
    inventory_system.display_inventory()

    # Removing a product
    inventory_system.remove_product(1)

    # Displaying inventory after removal
    inventory_system.display_inventory()

    # Updating quantity of a product
    inventory_system.update_quantity(2, 75)

    # Displaying inventory after update
    inventory_system.display_inventory()

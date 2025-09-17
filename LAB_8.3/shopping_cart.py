from typing import Dict, List, Tuple
class ShoppingCart:
    """A shopping cart class that manages items and calculates total cost."""
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, Tuple[float, int]] = {}  # item_name: (price, quantity)
    def add_item(self, item_name: str, price: float, quantity: int = 1) -> None:
        """Add an item to the shopping cart. 
        Args:
            item_name: Name of the item to add
            price: Price per unit of the item
            quantity: Number of units to add (default: 1)
        Raises:
            ValueError: If price or quantity is negative
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if item_name in self.items:
            # Update existing item
            current_price, current_quantity = self.items[item_name]
            self.items[item_name] = (price, current_quantity + quantity)
        else:
            # Add new item
            self.items[item_name] = (price, quantity)
    
    def remove_item(self, item_name: str, quantity: int = None) -> bool:
        """Remove an item or reduce its quantity from the shopping cart.
        
        Args:
            item_name: Name of the item to remove
            quantity: Number of units to remove. If None, removes all units.
        
        Returns:
            True if item was removed/reduced, False if item not found
        
        Raises:
            ValueError: If quantity is negative
        """
        if quantity is not None and quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        if item_name not in self.items:
            return False
        
        current_price, current_quantity = self.items[item_name]
        
        if quantity is None or quantity >= current_quantity:
            # Remove item completely
            del self.items[item_name]
        else:
            # Reduce quantity
            self.items[item_name] = (current_price, current_quantity - quantity)
        
        return True
    
    def get_total_cost(self) -> float:
        """Calculate the total cost of all items in the cart.
        
        Returns:
            Total cost as a float
        """
        total = 0.0
        for price, quantity in self.items.values():
            total += price * quantity
        return total
    
    def get_item_count(self) -> int:
        """Get the total number of items in the cart.
        
        Returns:
            Total quantity of all items
        """
        return sum(quantity for _, quantity in self.items.values())
    
    def get_cart_summary(self) -> List[str]:
        """Get a summary of all items in the cart.
        
        Returns:
            List of strings describing each item
        """
        summary = []
        for item_name, (price, quantity) in self.items.items():
            total_price = price * quantity
            summary.append(f"{item_name}: {quantity} x ${price:.2f} = ${total_price:.2f}")
        return summary
    
    def clear_cart(self) -> None:
        """Remove all items from the cart."""
        self.items.clear()
    
    def is_empty(self) -> bool:
        """Check if the cart is empty.
        
        Returns:
            True if cart is empty, False otherwise
        """
        return len(self.items) == 0


def _demo() -> None:
    """Demonstrate the ShoppingCart class functionality."""
    cart = ShoppingCart()
    
    print("=== Shopping Cart Demo ===")
    
    # Add items
    cart.add_item("Apple", 1.50, 3)
    cart.add_item("Banana", 0.80, 5)
    cart.add_item("Orange", 2.00, 2)
    
    print("\nItems added to cart:")
    for item in cart.get_cart_summary():
        print(f"  {item}")
    
    print(f"\nTotal items: {cart.get_item_count()}")
    print(f"Total cost: ${cart.get_total_cost():.2f}")
    
    # Remove some items
    print(f"\nRemoving 2 bananas...")
    cart.remove_item("Banana", 2)
    
    print("\nUpdated cart:")
    for item in cart.get_cart_summary():
        print(f"  {item}")
    
    print(f"\nTotal items: {cart.get_item_count()}")
    print(f"Total cost: ${cart.get_total_cost():.2f}")
    
    # Remove item completely
    print(f"\nRemoving all oranges...")
    cart.remove_item("Orange")
    
    print("\nFinal cart:")
    for item in cart.get_cart_summary():
        print(f"  {item}")
    
    print(f"\nTotal items: {cart.get_item_count()}")
    print(f"Total cost: ${cart.get_total_cost():.2f}")


def _cli() -> None:
    """Interactive CLI for the shopping cart."""
    cart = ShoppingCart()
    
    print("=== Shopping Cart CLI ===")
    print("Commands: add, remove, total, summary, clear, quit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip().lower()
            
            if command == "quit":
                break
            elif command == "add":
                item = input("Item name: ").strip()
                price = float(input("Price: $"))
                quantity = int(input("Quantity: "))
                cart.add_item(item, price, quantity)
                print(f"Added {quantity} {item}(s) at ${price:.2f} each")
            
            elif command == "remove":
                item = input("Item name: ").strip()
                quantity_input = input("Quantity to remove (or press Enter for all): ").strip()
                quantity = int(quantity_input) if quantity_input else None
                
                if cart.remove_item(item, quantity):
                    print(f"Removed {quantity if quantity else 'all'} {item}(s)")
                else:
                    print(f"Item '{item}' not found in cart")
            
            elif command == "total":
                print(f"Total cost: ${cart.get_total_cost():.2f}")
            
            elif command == "summary":
                if cart.is_empty():
                    print("Cart is empty")
                else:
                    print("Cart contents:")
                    for item in cart.get_cart_summary():
                        print(f"  {item}")
                    print(f"Total items: {cart.get_item_count()}")
                    print(f"Total cost: ${cart.get_total_cost():.2f}")
            
            elif command == "clear":
                cart.clear_cart()
                print("Cart cleared")
            
            else:
                print("Invalid command. Available: add, remove, total, summary, clear, quit")
        
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        _demo()
    else:
        _cli()

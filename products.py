class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.") 
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.activate = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: €{self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if not self.is_active() or quantity > self.quantity:
            raise Exception("Not enough stock or product inactive.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity
        

class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price

class Cart:
    def __init__(self): self.products = []
    def add(self, p): self.products.append(p)
    def remove(self, p): self.products.remove(p) if p in self.products else None
    def total_cost(self): return sum(p.price for p in self.products)

p1, p2 = Product("хлеб", 40), Product("молоко", 80)
cart = Cart()
cart.add(p1)
cart.add(p2)

print("Всего:", cart.total_cost())
cart.remove(p1)
print("После удаления:", cart.total_cost()) 

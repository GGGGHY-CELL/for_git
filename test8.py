class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар: {self.name}, цена: {self.price}"

item = Product("хлеб", 40)
print(item)  


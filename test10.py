class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __eq__(self, o): return self.x == o.x and self.y == o.y
    def __str__(self): return f"V({self.x}, {self.y})"

v1, v2, v3 = Vector(2, 3), Vector(4, 5), Vector(2, 3)

print("Сумма:", v1 + v2)  
print("v1 == v3:", v1 == v3)  
print("v1 == v2:", v1 == v2)  

# чуть чуть подсмотрела честно
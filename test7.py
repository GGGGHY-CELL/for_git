class Figure:
    def area(self): return 0

class Square(Figure):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2

class Circle(Figure):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14 * (self.radius ** 2)


print("Фигура:", Figure().area())   
print("Квадрат:", Square(5).area())
print("Круг:", Circle(3).area())    

# чутьчуть подсмотрела, ничего не понла и не понимаю
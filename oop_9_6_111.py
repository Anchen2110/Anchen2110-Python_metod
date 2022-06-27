from typing import Protocol,  runtime_checkable


@runtime_checkable
class Figure(Protocol):
    name: str

    def calculate_area(self)-> float:
        pass

    def calculate_perimeter(self) -> float:
        pass

# def show(figure: Figure):
#     if isinstance(figure, Figure):
#         print(f"S ({figure.name}) = {figure.calculate_area()}")
#         print(f"P ({figure.name}) = {figure.calculate_perimeter()}")
#     else:
#         print("Incompatible type")
def show(figure: Figure):
    print(f"S ({figure.name}) = {figure.calculate_area()}")
    print(f"P ({figure.name}) = {figure.calculate_perimeter()}")
    
class Square:
    name = "квадрат"

    def __init__(self, size):
        self.size = size

    def calculate_area(self):
        return self.size * self.size

    def calculate_perimeter(self):
        return 4 * self.size
        
    def set_color(self, color):
        """
        Класс может содержать собственные методы, 
        которые не относятся к протоколу.
        """
        self.color = color

# OK
show(Square(size=3.14))

class Circle:
    PI = 3.1415926
    name = "окружность"

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * self.PI * self.radius

show(Circle(radius=1))
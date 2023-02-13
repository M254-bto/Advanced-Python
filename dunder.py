class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    def __call__(self):
        print("A method in Vector class was called")

v1 = Vector(20, 30)
v2 = Vector(10, 20)
print(v1 + v2)

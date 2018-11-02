class Rectangle:
    def __init__(self, label, length, width):
        print('Rectangle __init__ \n')
        self.label = label
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Rectangle):
    def __init__(self, label, len):
        print('Square __init__')
        super().__init__(label, len, len)


squ1 = Square('squ1', 4)
Square.__init__: squ1
print(squ1)
Rectangle.__init__: squ1
print(squ1)

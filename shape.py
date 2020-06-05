import math

class Shape():
  def __init__(self,color,filled):
    self.color = color
    if filled == True:
        self.filled = "filled"
    else:
        self.filled = "not filled"

  def toString(self):
    return f"A Shape with color of {self.color} and {self.filled}"

shape = Shape("green",True)
print(shape.toString())
  
class Circle(Shape):
  def __init__(self,radius):
    self.__radius = radius
  
  @property
  def area(self):
    return 3.14*math.pow(self.__radius,2)
  @property
  def perimeter(self):
    return 2*3.14*self.__radius

  def toString(self,obj):
    return f"A Circle with radius={self.__radius}, which is a subclass of {obj.toString()}"

circle = Circle(5)
print(circle.toString(shape))

class Rectangle(Shape):
  def __init__(self,width,length):
    self.__width = width
    self.__length = length

  @property
  def area(self):
    return f"Area Rectangle-{self.__width*self.__length}"

  @property
  def perimeter(self):
    return f"Perimeter Rectangle-{2*(self.__width+self.__length)}" 

  def toString(self,obj2):
    return f"A Rectangle with width={self.__width} and length={self.__length}, which is a subclass of {obj2.toString()}"

rectangle = Rectangle(3,4)
print(rectangle.toString(shape))

class Square(Rectangle):
    def __init__(self,width,height):
        super().__init__(width,height)

square = Square(4,4)
print(square.area)
    
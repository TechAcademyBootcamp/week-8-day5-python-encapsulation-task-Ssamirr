class Vehicle():
    positionX = 50
    positionY = 50
    speed = 60
    isOn = False

    def __init__(self,numofWheels,color,engine):
      self.__numofWheels = numofWheels
      self.__color = color
      self.engine = engine

    def accelerate(self):
      self.speed +=1

    def moveForward(self,x,y):
      self.positionX += x
      self.positionY += y

    def moveBackwards(self,x,y):
      self.positionX -= x
      self.positionY -= y

    def ignition():
      if self.isOn == False:
        self.isOn = True
      if self.isOn == True:
        self.isOn = False

    @property
    def Color(self):
      print(self.__color)

    @Color.setter
    def Color(self,Color):
      self.__color = Color

    @property
    def NumofWheels(self):
      print(self.__numofWheels)
    
    @NumofWheels.setter
    def NumofWheels(self,num):
      self.__numofWheels = num
    
    def __str__(self):
      return f"NumofWheels={self.__numofWheels}\nColor={self.__color}\nEngine={self.engine}\nPositionX={self.positionX}\nPositionY={self.positionY}\nSpeed={self.speed}\nTamamlandi"


# vehicle = Vehicle(4,'black',3)
# vehicle.__str__()
# vehicle.accelerate()
# vehicle.moveForward(20,30)
# vehicle.moveBackwards(20,10)
# vehicle.setColor("Green")
# vehicle.setNumofWheels(6)
# vehicle.__str__()

class Motocycle(Vehicle):
  brand = "BMW"
  numofSeats = 3
  
  def __init__(self,color, engine, wheels, brand, seats):
    self.Mcolor = color
    self.Mengine = engine
    self.Mwheels = wheels
    self.__Mbrand = brand
    self.__Mseats = seats
  
  @property
  def Brand(self):
    return self.__Mbrand
  
  @property
  def numofSeats(self):
    return self.__Mseats
  
  @Brand.setter
  def Brand(self,brand):
    self.__Mbrand = brand

  @numofSeats.setter
  def numofSeats(self,numofSeats):
    self.__Mseats = numofSeats

  def accelerate():
    self.speed += 10

  def decelerate():
    self.speed -= 10

moto = Motocycle("red",2,2,"BMW",3)
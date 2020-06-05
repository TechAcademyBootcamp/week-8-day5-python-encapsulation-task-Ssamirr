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
    return f"Brand-{self.__Mbrand}"
  
  @property
  def numofSeats(self):
    return f"Seats-{self.__Mseats}"
  
  @Brand.setter
  def Brand(self,brand):
    self.__Mbrand = brand
    return f"New brand-{self.__Mbrand}"

  @numofSeats.setter
  def numofSeats(self,numofSeats):
    self.__Mseats = numofSeats
    return f"New seats-{self.__Mseats}"

  def accelerate(self):
    self.speed += 10
    return f"accelerate speed-{self.speed}"

  def decelerate(self):
    self.speed -= 10
    return f"decelerate speed-{self.speed}"


vehicle = Vehicle(4,'black',3)
print(vehicle.__str__())
vehicle.accelerate()
vehicle.moveForward(20,30)
vehicle.moveBackwards(20,10)
vehicle.Color = "Green"
vehicle.NumofWheels = 6
print("new")
print(vehicle.__str__())

moto = Motocycle("red",2,2,"BMW",3)
print("Motocycle info")
print(moto.Brand)
print(moto.numofSeats)
moto.Brand = "Bugatti"
print(moto.Brand)
moto.numofSeats = 2
print(moto.numofSeats)
print(moto.accelerate())
print(moto.decelerate())
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


vehicle = Vehicle(4,'black',3)
print(vehicle.__str__())
vehicle.accelerate()
vehicle.moveForward(20,30)
vehicle.moveBackwards(20,10)
vehicle.Color = "Green"
vehicle.NumofWheels = 6
print(vehicle.__str__())




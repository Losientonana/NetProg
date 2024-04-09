class Car :
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
        
    def speedUp(self,v):
        self.speed = self.speed + v
        return self.speed
    
    def speedDown(self,v):
        self.speed = self.speed - v
        return self.speed
    

myCar = Car("black",60)
print(myCar.color,myCar.speed)

myCar.speedUp(10)
print(myCar.color,myCar.speed)

myCar.speedDown(200)
print(myCar.color,myCar.speed)
class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

toyota=vehicle(240,18)
print("The max speed of a toyota is: ",toyota.max_speed)
print("The mileage of a toyota is: ",toyota.mileage)
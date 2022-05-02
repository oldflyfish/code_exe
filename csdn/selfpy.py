class car:
    speed = 20
    def drive(self,distance):
        time = distance / self.speed
        print(time)

bike = car()
#bike.spee = 60
bike.drive(80)
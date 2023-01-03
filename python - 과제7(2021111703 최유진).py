
class Car:
    color = ''
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


class Sedan(Car):
    seat = 0

    def getSeat(self):
        return self.seat

    def upSpeed(self, value):
        self.speed += value + 30


mySedan = Sedan()

mySedan.color = "빨강"
mySedan.speed = 10
mySedan. seat = 5

print("mySedan : %s, %d, %d" % (mySedan.color, mySedan.speed, mySedan.seat ))

mySedan.upSpeed(50)

print("mySedan : %s, %d, %d" % (mySedan.color, mySedan.speed, mySedan.seat ))

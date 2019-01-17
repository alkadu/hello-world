class Car:
    def __init__(self, speed, color):
        print(speed)
        print(color)
        self.speed=speed
        self.color= color
        print ('the __init__is called')

ford= Car(200, 'Red')
honda = Car(220, 'Blue')
audi = Car(250, 'Black')

# ford.speed = 200
# honda.speed = 220
# audi.speed = 250
#
# ford.color= 'Red'
# honda.color= 'Blue'
# audi.color= 'black'
#
# print (ford.speed)
# print (ford.color)


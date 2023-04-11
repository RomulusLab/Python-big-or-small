class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] =  self.position[0] + x
        print('New position:', self.position)


class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')

my_robot_dog = Robot_Dog('Marlow')
my_robot_dog.walk(21)
my_robot_dog.make_noise()

# This is an example of a "is a" relationship aka class inheritance
# The child Robot_Dog(Robot) is inheriting the __init__ method of the parent
# It also has its own method that will be appended
# The 'my_robot_dog' is a class object which will use the defined 'init' (which contains name, position and print)
# 'walk', and 'make_noise' method defined in the child

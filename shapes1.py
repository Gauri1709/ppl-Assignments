import turtle
r = turtle.getscreen()
g = turtle.Turtle()


class shape:
    def __init__(self, sides = 0, length = 34):
           self.sides = sides
           self.length = length

class polygon(shape):
    def info(self):
           print("In geometry, a polygon can be defined as a flat or plane, two-dimentional with straight sides.")

class square(polygon):
    def show(self):
           g.fd(self.length)
           g.rt(90)
           g.fd(self.length)
           g.rt(90)
           g.fd(self.length)
           g.rt(90)
           g.fd(self.length)
           g.rt(90)


class pentagon(polygon):
    def show(self):
           for i in range(5):
              g.forward(self.length)
              g.right(72)

class hexagon(polygon):
    def show(self):
          for i in range(6):
              g.forward(self.length)
              g.right(60)


class octagon(polygon):
    def show(self):
          for i in range(8):
              g.forward(self.length)
              g.right(45)


class triangle(polygon):
   def show(self):
              g.forward(self.length)
              g.right(120)
              g.forward(self.length)
              g.right(120)
              g.forward(self.length)  
              
t = pentagon()
t.info()
t.show()

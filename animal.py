class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes


class vertebrates(Animals):
    def back_bone(self):
        print("With backbone")

class reptile(vertebrates):
    def blood_temp(self):
        print("cold blooded animal")
    
        
class snake(reptile):
    def speak(self):
        print("Hissing")
    def colour(self):
        print("They are  found in various colour")
        
class turtule(reptile):
    def speak(self):
        print("Hissing")
    def colour(self):
        print("Shells are commonly colored brown, black, or olive green.")
        
class lizard(reptile):
    def speak(self):
        print("chemical communication")
    def colour(self):
        print("able to change colour")


                        
class mammal(vertebrates):
    def gland(self):
        print("Presence of mammary gland")

class man(mammal):
    def speak(self):
        print("Speak in different language")
        
class elephant(mammal):
    def speak(self):
        print("dummyvalue")
    def colour(self):
        print("Grey")
        
class whale(mammal):
    def speak(self):
        print("whistles")
    def weight(self):
        print("more than 200 ton")


        

class Invertebrates(Animals):
    
    def back_bone(self):
        print("without backbone")

        
class snail(Invertebrates):
    def food(self):
        print("fungi")
    def colour(self):
        print("ranging from light to dark brown")
        
class ant(Invertebrates):
    def speak(self):
        print("chirp")
    def colour(self):
        print("red or black")
        
class cocroach(Invertebrates):
    def speak(self):
        print("stridulation")
    def colour(self):
        print("reddish-brown to black in color")
        
class bees(Invertebrates):
    def speak(self):
        print("buzz")
    def colour(self):
        print("creatures with golden-yellow colors and brown bands.")

A1=Animals(4, 3)
S1 = snail()
S1.food()
S1.colour()
S2 = ant()
S2.speak()
print(S1.eyes)
print(S2.legs)



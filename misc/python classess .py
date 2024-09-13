class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name},{self.age}"

class student(person):
    def __init__(self, name, age,gyear):
        super().__init__(name, age)
        self.gyear = gyear
    def __str__(stu):
        return f"{stu.name},{stu.age},{stu.gyear}"

class c:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
     if self.a <= 20:
            x = self.a
            self.a += 1
            return x
     else:
            raise StopIteration


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")
    
class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object


f = open("test.txt","a")
f.write(car1.brand)

f.close()
print("made file")
f = open("test.txt","r")

print(f.read(8))




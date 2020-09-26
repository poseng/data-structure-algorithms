class Dog:
    # # This is the constructor for the class. It is called whenever a Dog
    # # object is created. The reference called "self" is created by python and made
    #  to point to the space for the newly created object.
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
    # This is an accessor method
    def speak(self):
        return self.speakText
    # Here is an accessor method as well.
    def getname(self):
        return self.name
    # accessor method for birthday
    def birthDate(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)
    # This is a mutator method.
    def changeBark(self, bark):
        self.speakText = bark
    # method overloading to create a new puppy
    def __add__(self, other):
        return Dog("Puppy of " + self.name + " and " + other.name,
                   self.day + other.day, self.month + other.month, self.year + other.year,
                   self.speakText + " " + other.speakText)
def main():
    boyDog = Dog("Meta", 25, 5, 2019, "Wofofo")
    girlDog = Dog("Cheata", 23, 2, 2020, "Barkbark")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeBark("wowowf")
    print(boyDog.speak())
    childDog = boyDog + girlDog
    print(childDog.speak())
    print(childDog.birthDate())
    print(childDog.getname())

if __name__ == "__main__":
    main()
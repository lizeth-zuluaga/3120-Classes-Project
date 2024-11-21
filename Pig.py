//Lizeth Zuluaga

from Animal import Animal

class Pig(Animal):
    def __init__(self, name):
        super().__init__(name, species="pig")
    def speak(self):
        print("hoy,hoy,hoy!")
        
def main():
    pig =Pig("Lola")
    pig.display_info()
    print(pig.speak())
if __name__ == "__main__":
        main()

import Animal
class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, species="birds")

    def speak(self):
        print("Chick!")

def main():
    chicken = Chicken("Lola")
    chicken.display_info()
    print(chicken.speak())

if __name__ == "__main__":
    main()
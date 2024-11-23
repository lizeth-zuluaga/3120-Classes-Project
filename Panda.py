class Panda(Animal): 
    def __init__(self, name):
        super().__init__(name, species ="panda")

    def speak(self):
        print("Chomp Chomp O_O")

def main():
    panda = Panda("Panda")
    panda.display_info()
    print(panda.speak())
if __name__ == "__main__":
    main()
  
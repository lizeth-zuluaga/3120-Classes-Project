#!/usr/bin/env python
# coding: utf-8

# ###
# 3120/ group 2 

# In[1]:


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Animal Name: {self.name}")
        print(f"Species: {self.species}")


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, species="birds")

    def speak(self):
        print("Chick!")

def main():
    chicken = Chicken("Lola")
    chicken.display_info()
    chicken.speak()

if __name__ == "__main__":
    main()

# In[ ]:





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


# In[2]:


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")


# In[3]:


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")


# In[4]:


class Parrot(Animal):
    def __init__(self, name):
        super().__init__(name, species="Parrot")


# In[13]:


class Pig(Animal):
    def __init__(self, name):
        super().__init__(name, species="pig")


# In[14]:


def main():
    dog = Dog("Bella")
    cat = Cat("Kitty")
    parrot = Parrot("Paco")
    pig = Pig("Lola")
    
    dog.display_info()
    print() 
    cat.display_info()
    print()  
    parrot.display_info()
    print()
    pig.display_info()


# In[15]:


if __name__ == "__main__":
    main() 


# In[ ]:





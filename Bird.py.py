#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Animal import Animal


# In[9]:


x = Animal()
x.talk()


# In[12]:


class Bird(Animal): #child class
    def __init__(self, name):
        super().__init__(name, species ="bird")
        print("Hello I am a bird.")

    def speak(self):
        print("Tweet!")

def main():
    bird = Bird("Tweety")
    bird.display_info()
    print(bird.speak())
if __name__ == "__main__":
    main()
    


# In[ ]:





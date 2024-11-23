{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f39c0ef8-eea6-44d2-878c-8e5a7cefcea9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Animal Name: Panda\n",
      "Species: panda\n",
      "Chomp Chomp O_O\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "class Panda(Animal): \n",
    "    def __init__(self, name):\n",
    "        super().__init__(name, species =\"panda\")\n",
    "\n",
    "    def speak(self):\n",
    "        print(\"Chomp Chomp O_O\")\n",
    "\n",
    "def main():\n",
    "    panda = Panda(\"Panda\")\n",
    "    panda.display_info()\n",
    "    print(panda.speak())\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6471073a-9c64-489a-883c-4f7d502100e3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

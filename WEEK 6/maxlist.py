#Your task is to implement a class that maintains a list of numbers and has a method for efficiently finding the largest number on the list.
#In a file maxlist.py, implement the class MaxList with the following methods:

#append(number): add a number to the end of the list
#max(): return the largest number

#You may assume that the list has at least one number when the method max is called. Both methods should work efficiently in O(1) time.

class MaxList:
    def __init__(self):
        self.lista = []       
        self.massimo = None

    def append(self, numero):
        self.lista.append(numero)
        if self.massimo is None or numero > self.massimo:
            self.massimo = numero

    def max(self):
        return self.massimo

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8
    numbers = MaxList()
    total = 0

    for i in range(10**5):
        numbers.append(i * 999983 % 10**9)
        total += numbers.max()
    print(total) # 99498381797517
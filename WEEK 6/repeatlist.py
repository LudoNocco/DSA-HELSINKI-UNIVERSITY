#Your task is to implement a class that maintains a list of numbers and has an efficient method that reports if some number occurs more than once on the list.
#In a file repeatlist.py, implement the class RepeatList with the following methods:

#append(number): add a number to the end of the list
#repeat(): return True if some number repeats on the list, otherwise return False

#Both methods should work in O(1) time

class RepeatList:
    def __init__(self):
        self.lista = []
        self.visti = set()  
        self.duplicati = set()   

    def append(self, numero):
        self.lista.append(numero)
        if numero in self.visti:
            self.duplicati.add(numero)
        else:
            self.visti.add(numero)

    def repeat(self):
        return len(self.duplicati) > 0

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True

    numbers = RepeatList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 12345)
        if numbers.repeat():
            total += 1
    print(total) # 87655
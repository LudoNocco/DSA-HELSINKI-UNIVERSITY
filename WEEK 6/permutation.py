#A list is a permutation if it contains the numbers 1,2,\dots,n exactly once each. For example, the lists [1], [2,1] and [3,1,2,4] are permutations.
#In a file permutation.py, implement the class PermutationTracker with the following methods:

#append(number): add number to the end of the list
#check(): return True, if the list is a permutation, and False otherwise

#The time complexity of both methods should be O(1).

class PermutationTracker:
    def __init__(self):
        self.n = 0
        self.somma = 0
        self.somma_quadrati = 0

    def append(self, numero):
        self.n += 1
        self.somma += numero
        self.somma_quadrati += numero * numero

    def check(self):
        somma_attesa = self.n * (self.n + 1) // 2
        somma_quad_attesa = self.n * (self.n + 1) * (2 * self.n + 1) // 6
        return self.somma == somma_attesa and self.somma_quadrati == somma_quad_attesa

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False

    tracker = PermutationTracker()
    
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000
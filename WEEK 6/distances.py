#Your task is to implement a class that maintains a list of numbers and has a method for efficiently computing the sum of distance between all pairs of occurrences of a given number.
#For example, when the list is [1,2,1,3,3,1,2,1], the distances for the number 1 are:

#positions 0 and 2: distance 2
#positions 0 and 5: distance 5
#positions 0 and 7: distance 7
#positions 2 and 5: distance 3
#positions 2 and 7: distance 5
#positions 5 and 7: distance 2

#Thus the sum of the distances is 2+5+7+3+5+2=24.
#In a file distances.py, implement the class DistanceTracker with the methods:

#append(number): add number to the end of the list
#sum(number): return the sum of distance for number

#Both methods should work in O(1) time.

class DistanceTracker:
    def __init__(self):
        self.pos = 0
        self.dati = {}
    def append(self, numero):
        if numero not in self.dati:
            self.dati[numero] = [0, 0, 0]
        cnt, somma, dist = self.dati[numero]
        nuovo = cnt * self.pos - somma
        self.dati[numero] = [cnt + 1, somma + self.pos, dist + nuovo]
        self.pos += 1
    def sum(self, numero):
        if numero not in self.dati:
            return 0
        return self.dati[numero][2]
    
if __name__ == "__main__":
    tracker = DistanceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    tracker.append(3)
    tracker.append(1)
    tracker.append(2)
    tracker.append(1)

    print(tracker.sum(1)) # 24
    print(tracker.sum(2)) # 5
    print(tracker.sum(3)) # 1

    tracker.append(1)
    tracker.append(2)
    tracker.append(3)

    print(tracker.sum(1)) # 42
    print(tracker.sum(2)) # 16
    print(tracker.sum(3)) # 14

    tracker = DistanceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(1)
        total += tracker.sum(1)
    print(total) # 4166749999583325000
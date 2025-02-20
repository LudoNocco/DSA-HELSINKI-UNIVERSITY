class Stato:
    def __init__(self):
        self.n = 0
        self.x = 0
        self.y = 0
        self.xx = 0
        self.xy = 0
        self.yy = 0

class DataAnalyzer:
    def __init__(self):
        self.s = Stato()
    def add_point(self, x, y):
        self.s.n += 1
        self.s.x += x
        self.s.y += y
        self.s.xx += x*x
        self.s.xy += x*y
        self.s.yy += y*y
    def calculate_error(self, a, b):
        return self.s.yy - 2*a*self.s.xy + a*a*self.s.xx - 2*b*self.s.y + 2*a*b*self.s.x + b*b*self.s.n

if __name__ == "__main__":
    analyzer = DataAnalyzer()

    analyzer.add_point(1, 1)
    analyzer.add_point(3, 2)
    analyzer.add_point(5, 3)
    print(analyzer.calculate_error(1, 0)) # 5
    print(analyzer.calculate_error(1, -1)) # 2
    print(analyzer.calculate_error(3, 2)) # 293

    analyzer.add_point(4, 2)
    print(analyzer.calculate_error(1, 0)) # 9
    print(analyzer.calculate_error(1, -1)) # 3
    print(analyzer.calculate_error(3, 2)) # 437

    analyzer = DataAnalyzer()
    total = 0
    for i in range(10**5):
        analyzer.add_point(i, i % 100)
        total += analyzer.calculate_error(i % 97, i % 101)
    print(total) # 25745448974503313754828

def find_number(numbers):
    from collections import Counter
    c=Counter(numbers)
    for k,v in c.items():
        if v==1:
            return k

if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2

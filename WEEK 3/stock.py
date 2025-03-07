def find_profits(prices):
    ans=[]
    m=float('inf')
    for p in prices:
        if p<m:
            m=p
        r=p-m
        if r<0:
            r=0
        ans.append(r)
    return ans

if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 1, 2, 3]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 0, 0, 0]
    print(find_profits([2, 4, 1, 3])) # [0, 2, 0, 2]
    print(find_profits([1, 1, 5, 1])) # [0, 0, 4, 0]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 1, 3, 0, 3]

    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 1, 2, 3, 4]
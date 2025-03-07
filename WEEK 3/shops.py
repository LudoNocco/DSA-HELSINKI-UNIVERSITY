def find_distances(street):
    shop_positions=[]
    for i,ch in enumerate(street):
        if ch=='1':
            shop_positions.append(i)
    n=len(street)
    dist=[0]*n
    j=0
    for i in range(n):
        while j<len(shop_positions)-1 and abs(shop_positions[j+1]-i)<=abs(shop_positions[j]-i):
            j+=1
        dist[i]=abs(shop_positions[j]-i)
    return dist

if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663

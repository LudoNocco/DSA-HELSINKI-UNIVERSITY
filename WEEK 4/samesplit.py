# You are given a list of integers. Your task is to count how many ways the list can be split into two parts so that every integer on the list occurs both in the left part and in the right part.
# For example, the answer for the list [1,2,1,2,1,2] is 3, because the valid splits are [1,2]+[1,2,1,2], [1,2,1]+[2,1,2] and [1,2,1,2]+[1,2].
# In a file samesplit.py, implement the function count_splits that takes a list as a parameter and returns the number ways to split the list.
# The function should be efficient even for long lists. The last two test cases in the code template are long lists and the function should finish quickly in these cases too.

def count_splits(numbers):
    prima_occ = {}
    ultima_occ = {}
    
    for i, num in enumerate(numbers):
        if num not in prima_occ:
            prima_occ[num] = i
        ultima_occ[num] = i
    
    for num in prima_occ:
        if prima_occ[num] == ultima_occ[num]:
            return 0
    
    max_prima = max(prima_occ.values())
    min_ultima = min(ultima_occ.values())
    
    return max(0, min_ultima - max_prima)

if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1
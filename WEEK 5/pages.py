# You are given a list of page numbers. Your task is to construct a string that describes the page ranges compactly.
# If the list contains all page numbers in the range a \dots b, this should be presented in the form a–b. If the list contains an isolated page number, it should be presented as a single number. If the list contains multiple page ranges, they should be presented as an ordered list separated by commas. Repeated page numbers should be included only once.
# For example, if the list is [3,2,9,4,3,6,9,8], the desired representation is 2-4,6,8-9.
# In a file pages.py, implement the function create_string that takes a list of page numbers as a parameter and returns a string of page ranges as described above.
# You should implement the function so that it does not modify the input list. The last test case in the code template prints the list after calling the function and it should be the same as before the call. The same requirement applies to all tasks this weeks.

def create_string(pagine):
    pagine_uniche = sorted(set(pagine))
    intervalli = []
    inizio = fine = pagine_uniche[0]

    for num in pagine_uniche[1:]:
        if num == fine + 1:
            fine = num
        else:
            intervalli.append(f"{inizio}-{fine}" if inizio != fine else str(inizio))
            inizio = fine = num

    intervalli.append(f"{inizio}-{fine}" if inizio != fine else str(inizio))
    return ",".join(intervalli)

if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]

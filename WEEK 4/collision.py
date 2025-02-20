# Consider again the hash function of the earlier task:

# (c_0 A^{n-1} + c_1 A^{n-2} \cdots + c_{n-1} A^0) \bmod M

# The parameters are the same as before: A=23 ja M=2^{32}.
# In a file collision.py, implement the function find_other that takes a string as a parameter and returns a different string with the same hash value.
# The input string consists of the characters a–z and has at most 100 characters. The output string should satisfy the same requirements.
# The function should be efficient and return a different string immediately.

def hash_value(stringa):
    h = 0
    for c in stringa:
        h = (h * 23 + (ord(c) - 97)) % (2**32)
    return h
def find_other(stringa):
    H = hash_value(stringa)
    L = 9
    candidato = ""
    for i in range(L):
        d = H // (23 ** (L - 1 - i))
        candidato += chr(d + 97)
        H %= 23 ** (L - 1 - i)
    if candidato == stringa:
        return "a" + candidato
    return candidato

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682

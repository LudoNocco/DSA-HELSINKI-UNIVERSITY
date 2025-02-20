def merge_sort(indici, comparatore):
    if len(indici) <= 1:
        return indici
    mid = len(indici) // 2
    sin = merge_sort(indici[:mid], comparatore)
    des = merge_sort(indici[mid:], comparatore)
    ris = []
    i = j = 0
    while i < len(sin) and j < len(des):
        if comparatore.smaller(sin[i], des[j]):
            ris.append(sin[i])
            i += 1
        else:
            ris.append(des[j])
            j += 1
    ris.extend(sin[i:])
    ris.extend(des[j:])
    return ris

def find_list(comparatore):
    n = comparatore.list_size()
    indici = list(range(n))
    ordinati = merge_sort(indici, comparatore)
    risultato = [0] * n
    for pos, i in enumerate(ordinati):
        risultato[i] = pos + 1
    return risultato

if __name__ == "__main__":
    import math
    class Comparer:
        def __init__(self, numeri):
            self.numeri = numeri
            self.cont = 0
            n = len(numeri)
            self.limite = n * math.floor(math.log2(n))
        def list_size(self):
            return len(self.numeri)
        def smaller(self, a, b):
            self.cont += 1
            if self.cont > self.limite:
                raise RuntimeError("troppi confronti")
            return self.numeri[a] < self.numeri[b]
    c = Comparer([3,1,2,4])
    print(find_list(c))
    c = Comparer([1,6,2,5,3,4])
    print(find_list(c))

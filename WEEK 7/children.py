class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_children(nodo):
    lista = [len(nodo.children)]
    for childreno in nodo.children:
        lista += count_children(childreno)
    lista.sort()
    return lista

if __name__ == "__main__":
    albero1 = Node(1, [Node(4, [Node(3), Node(7)]),
                       Node(5),
                       Node(2, [Node(6)])])
    print(count_children(albero1))
    albero2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_children(albero2))
    albero3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_children(albero3))

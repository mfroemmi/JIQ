# Aufgabe: Zwei Zahlen addieren, die als Liste gespeichert sind.

class Node():
    def __init__(self, x):
        self.foo = x
        self.next = None

class Add:
    def rekursiv(self, zahl1, zahl2):
        val = zahl1.foo + zahl2.foo
        res = Node(val)

        if zahl1.next and zahl2.next:
            res.next = self.rekursiv(zahl1.next, zahl2.next)
        return res

l1 = Node(6)
l1.next = Node(2)
l1.next.next = Node(3)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)

result = Add().rekursiv(l1, l2)
while result:
    print(result.foo)
    result = result.next




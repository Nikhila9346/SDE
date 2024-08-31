class MyHash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for x in range(b)]
    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)
        print(self.table)
    def delete(self, x):
        i = x % self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)
        print(self.table)
    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]
    

h = MyHash(7)
h.insert(70)                  #[[70], [], [], [], [], [], []]
h.insert(71)                  #[[70], [71], [], [], [], [], []]
h.insert(9)                   #[[70], [71], [9], [], [], [], []]
h.insert(56)                  #[[70, 56], [71], [9], [], [], [], []]
h.insert(72)                  #[[70, 56], [71], [9, 72], [], [], [], []]
print(h.search(56))           #True
h.delete(56)                  #[[70], [71], [9, 72], [], [], [], []]
print(h.search(56))           #false
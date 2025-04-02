class IntSet:
    def __init__(self):
        self._elements = set()
    def insert(self,x):
        self._elements.add(x)
    def __iter__(self):
        for e in self._elements:
            yield e
    

iset = IntSet()
iset.insert(5)
iset.insert(7)
iset_iter = iset.__iter__()
print(type(iset_iter))
print(next(iset_iter))
print(iset_iter.__next__())
print(iset_iter.__next__())

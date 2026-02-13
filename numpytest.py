import numpy as np
class Vector():
    def __init__(self, data):
        if type(data) != list:
            raise TypeError("data ha de ser una llista")
        self.data = data
    def __len__(self):
        return len(self.data)
    def norma(self):
        return np.linalg.norm(self.data)
    def unitari(self):
        if self.norma() != 0:
            return [float(a / np.linalg.norm(self.data)) for a in self.data]
        else:
            return "norma = 0"
    def producte(self, w):
        if isinstance(w, Vector) and len(self) == len(w):
            m = 0
            for l in range(len(self.data)):
                m += self.data[l] * w.data[l]
            return m
        else:
            return None

v = Vector([1, 2])
w = Vector([2, 4])
print(len(v), len(w))
print(v.norma(), w.norma())
print(v.unitari(), w.unitari())
print(v.producte(w))
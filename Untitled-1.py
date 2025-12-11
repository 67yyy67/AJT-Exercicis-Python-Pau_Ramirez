A = [[2, 3, 4, 5],
     [2, 2, 2, 2],
     [2, 3, 4, 4],
     [1, 0, 0, 1]]


NovA = A
for a in range(len(A)-2):
    for b in range(len(A[a])):
        NovA.pop(a)
        for c in range(len(NovA)):
            NovA[c].pop(b)

def detmat(A):
    if len(A) != len(A[0]):
        print("no determinable")
    elif len(A) < 2:
        detA = A[0][0]
    else:
        NovA = A
        Aij = []
        detAij = []
        currentAij = A
        detA = 0
        #funció per conseguir Aij, traient la columna j  i la fila i de la matriu
        def funciomatAij(B, i, j):
            Bij = B
            Bij.remove(Bij[i])
            for a in range(len(NovA)):
                Bij[a].remove(Bij[a][j])
            return Bij
        
        def funciodetmat(A):
            if len(A) == 1:
                detA = A[0][0]
            else:
                for i in range(len(A)):
                    detA += (funciodetmat(funciomatAij(A, i, 0)))*(-1)**(i + 0)
            return detA   
    return detA


                    
            
x = [[2, 3, 4, 5],
     [2, 2, 2, 5],
     [2, 3, 4, 5],
     [2, 3, 4, 5]]
print(detmat(x))

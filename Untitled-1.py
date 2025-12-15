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
        #funció per expandir la matriu Aij a A. A es A i B es Aij 
        def funciomatdetAijaA(B, A, i, j):
            Cij = (B[0][0]*B[1][1]+B[0][1]*B[1][0])*(-1)**(i + j)
            detCij = A[i][j]*Cij
            return detCij
        while True:
            if len(NovA) == 2:
                detA = NovA[0][0]*NovA[1][1]+NovA[0][1]*NovA[1][0]
                break
            elif len(NovA) == 3:
                for a in range(len(A)):
                    for b in range(len(A[a])):
                        detA = detA + funciomatdetAijaA(funciomatAij(A, a, b), A, a, b)
                break
            else:
                pass          
    return detA


                    
            
x = [[2, 3, 4],
     [2, 2, 2],
     [2, 3, 4],]
print(detmat(x))

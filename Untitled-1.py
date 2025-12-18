A = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]
jugador = "X"
def canvijug(a):
    if a == "X":
        b = "O"
    else:
        b = "X"
    return b
def mostramat(A):
    for a in range(len(A)):
        print(A[a])
def posarfitxa(A, jug):
    try: 
        a = int(input("a quina fila vols posar fitxa?"))
        b = int(input("a quina columna vols posar fitxa?"))
        if ((a or b) not in range(1, 4)) or A[a-1][b-1] != "-":
            print("posició no válida")
            return posarfitxa(A, jug)
        else:
            A[a-1][b-1] = jug
    except:
        print("posició no válida")
        return posarfitxa(A, jug)
def clear(A):
    for a in range(len(A)):
        for b in range(len(A[a])):
            A[a][b] = "-"
punts = {"O" : 0, "X" : 0, "-" : 0}
while True:
    final = False
    print("--------------")
    posarfitxa(A, jugador)
321    mostramat(A)
    for a in range(len(A)):
        if A[a][0] == A[a][1] and A[a][2] == A[a][1] and A[a][0] != "-":
            print(f"ha guanyat el jugador {jugador}")
            final = True
            vic = f"{jugador}"
        elif A[0][a] == A[1][a] and A[1][a] == A[2][a] and A[0][a] != "-":
            print(f"ha guanyat el jugador {jugador}")
            final = True
            vic = f"{jugador}"
    if (A[0][0] == A[1][1] and A[1][1] == A[2][2]) or (A[2][0] == A[1][1] and A[1][1] == A[0][2]) and A[1][1] != "-":
        print(f"ha guanyat el jugador {jugador}")
        final = True
        vic = f"{jugador}"
    if "-" not in (A[0] and A[1] and A[2]):
        print(f"Empat")
        final = True
        vic = "-"
    if final == True:
        input_seguir = input("Voleu seguir jugant? Y/N")
        punts[vic] += 1
        print(f"X ha guanyat {punts["X"]} cops, O ha guanyat {punts["O"]} cops, i heu empatat {punts["-"]} cops")
        if input_seguir == "Y":
            clear(A)
            jugador = "X"
            continue
        else:
            print("moltes gracies per jugar")
            break
    jugador = canvijug(jugador)



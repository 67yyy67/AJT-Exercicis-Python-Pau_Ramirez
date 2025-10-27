tolerancia = 10**(-5)
m = [1, -1]     
def f(x):
    return 2*x + 1
while True:
    if abs(m[0] - m[1]) <= tolerancia:
        print(f"La funcio definida es 0 a {f(m[1])}")
        break
    elif abs(f(m[0])) <= tolerancia:
        print(f"La funcio definida es 0 a {f(m[0])}")
        break
    elif abs(f(m[1])) <= tolerancia:
        print(f"La funcio definida es 0 a {f(m[1])}")
        break
    elif f(m[0])*f(m[1]) < 0:
        x = (m[0] + m[1])/2
        if abs(f(x)) <= tolerancia:
            print(f"La funcio definida es 0 a {x}")
            break
        elif f(x)*f(m[0]) < 0:
            m[1] = x
            continue
        elif f(x)*f(m[1]) < 0:
            m[0] = x
            continue
    else:
        print("no hi ha cap 0 a l'interval definit")
        break


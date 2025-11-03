n = int(input("introdueix un nombre enter més gran o igual que 0"))
Triangle = []
for a in range(0, n):
    Triangle.append([])
    Triangle[a].append(1)
    for b in range(0,a):
        Triangle[a].append(Triangle[a-1][b-1]+Triangle[a-1][b])
    Triangle[a].append(1)



print(Triangle)


def fep(n, w, movements):
    g = [['.' for i in range(n)] for j in range(w)]
    cx, cy = 0, 0
    g[cy][cx] = '*' 
    for move in movements:
        if move == 'R' and cx < n - 1:
            cx += 1
        elif move == 'L' and cx > 0:
            cx -= 1
        elif move == 'B':
            cy += 1
        g[cy][cx] = '*'
    for i in range(w):
         print(' '.join(g[i]))
    if cx != n - 1:
         print("There's no way out!")

n = int(input())
K = []
m = 0
while True:
    d = input()
    if d != "END":
        K.append(d)
        if d == "B":
            m += 1
    else:
        break
fep(n, m + 1, K)

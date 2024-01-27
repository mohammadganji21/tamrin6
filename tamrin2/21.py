def fep(n, w, movements):
    g = [['.' for _ in range(n)] for _ in range(w)]
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
    
    for row in g:
        print(' '.join(row))
    
    if cx != n - 1:
        print("There's no way out!")

def main():
    n = int(input())
    movements = []
    
    while True:
        move = input()
        if move != "END":
            movements.append(move)
        else:
            break

    fep(n, len(movements) + 1, movements)

if __name__ == "__main__":
    main()


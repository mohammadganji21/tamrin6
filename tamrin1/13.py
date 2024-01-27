def jaamtabe(a, b):
    while b != 0:
        mmd = a & b
        a = a ^ b
        b = mmd << 1
    return a

def main():
    n = int(input())
    m = int(input())
    k = int(input())

    result = jaamtabe(n, m)

    print(result)

    if result == k:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()

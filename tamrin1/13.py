def jaamtabe(a,b):
    while b != 0:
        mmd = a & b
        a = a ^ b
        b = mmd << 1
    return a

    
n = int(input())

m = int(input())

k = int(input())

javabejaametabe = jaamtabe(n,m)


if javabejaametabe == k :
    print(javabejaametabe)
    print('YES')
else :
    print(javabejaametabe)
    print('NO')
def tabe_tashkhis_adad_aval(adadvorudi):
    if adadvorudi < 2:  
        return '0'
    for i in range(2, int(adadvorudi ** 0.5) + 1):
        if adadvorudi % i == 0:
            return '0'
    return '1'
a, b = map(int, input().split())
tedad_adad_aval = 0

if a < b:
    for i in range(a, b + 1):
        if tabe_tashkhis_adad_aval(i) == '1':
            tedad_adad_aval += 1
    print('main order - amount: ' + str(tedad_adad_aval))
elif a >= b:
    for i in range(b, a + 1):
        if tabe_tashkhis_adad_aval(i) == '1':
            tedad_adad_aval += 1
    print('reverse order - amount: ' + str(tedad_adad_aval))
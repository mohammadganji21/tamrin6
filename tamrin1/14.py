a = int(input())
b = int(input())
baze_taghirat = int(a) ^ int(b)
asad = bin(baze_taghirat).count('1')
print(asad)
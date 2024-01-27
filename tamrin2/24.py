shomare_radif = int(input())
mosalas = [[1]]

for i in range(1, shomare_radif):
    radif = [1]
    for j in range(1, i):
        radif.append(mosalas[i-1][j-1] + mosalas[i-1][j])
    radif.append(1)
    mosalas.append(radif)
    
for radif in mosalas:
    print("" * (shomare_radif-len(radif)))
    for shomare in radif:
         print(f"{shomare} " , end ="" )
    print()
# by mohammad_ganji(vdds)
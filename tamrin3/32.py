list_of_numbers = list(map(int, input().split()))
result_we_want = input()
result_we_want = int(result_we_want)
nonsorted, sorted = {} , []

#checking the result of our sum with the result that system want

for i , j in enumerate(list_of_numbers):
    important_number = (result_we_want - j)
    if important_number in nonsorted:
        sorted . append(nonsorted[important_number] + i)
    nonsorted[j] = i

if sorted:
    sorted . sort()
    for i in sorted:
        print(i)

else:
    print("Not Found!")
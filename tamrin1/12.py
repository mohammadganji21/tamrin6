#by ganji

def tabe_tabdil_be_binary(n): 
    return "{:032b}".format(int(n))

rightside = str(input())
leftside = str(input())

tedad_afrad = int(input())

leftside = str(tabe_tabdil_be_binary(int(leftside)))
rightside = str(tabe_tabdil_be_binary(int(rightside)))

binary_tamam_afrad = str(leftside)+str(rightside)

list_print_nahayi=[]

for i in range(tedad_afrad):

    m = int(input())

    if binary_tamam_afrad[-m-1]=='0':
        list_print_nahayi.append('no')

    else:
        list_print_nahayi.append('yes')


for a in range(len(list_print_nahayi)):
    print(list_print_nahayi[a])
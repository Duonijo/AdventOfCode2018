content = open('input.txt', 'r').read()
list = []
final_list = []
min = int()
#print(content)
def reduce(list_base):
    i = 0
    max = len(list_base)
    print("ckoi la liste : {}".format(list_base))
    while i < max-1:
        if  list_base[i]+32 == list_base[i+1] or list_base[i]-32 == list_base[i+1]:
            print('va etre remove {} et {}'.format(chr(list_base[i]), chr(list_base[i+1])))
            del list_base[i+1]
            del list_base[i]

            i = 0
            max = len(list_base)
        else : i+=1
    list_base.remove(10)
    return list_base

def minimum(list_base,content):
    min = len(list_base)
    print(list_base)
    for letter in range(65,90):
        try:
            print(letter)
            print(list_base)

            list_base[:] = (x for x in list_base if x != letter and x!= (letter+32))
            print(list_base)
            print("list_base : {}".format(list_base))

        except:
            print("null")
        list_base = reduce(list_base)
        print("liste base : {} \n".format(list_base))
        if len(list_base) < min:
            min = len(list_base)
            print("le min est : {}".format(min))
        list_base = []
        for i in range(len(content)):
            list_base.append(ord(content[i]))
    return min

#LISTE DE BASE A PARTIR DE L'INPUT
for i in range(len(content)):
    list.append(ord(content[i]))

min = minimum(list,content)
print(min)

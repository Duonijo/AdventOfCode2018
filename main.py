content = open('input.txt', 'r').read()
content = content.split()
list = []
word = ''
nb_ligne = 1323
list_imprim = [[0]*nb_ligne for i in range(nb_ligne)]
nb_X = 0


#list with numbers and X
def changelist(ligne, left, top, tall, wide, list_imprim):
    for i in range(wide):
        for j in range(tall):
            if list_imprim[top+i][left+j] == 0:
                list_imprim[top+i][left+j]  =1
            else:
                list_imprim[top+i][left+j]  = 2


#Count X
def howManyX(list_imprim, nb_X):
    for i in range(len(list_imprim)):
        for j in range(len(list_imprim)):
            if list_imprim[i][j] == 2:
                nb_X += 1
    return nb_X

for i in range(len(content)):
    word = ""
    for j in range(len(content[i])):
        if   48 <= ord(content[i][j]) and ord(content[i][j]) <= 57:
            word = "{}{}".format(word, content[i][j])
        elif ord(content[i][j]) == 44 or ord(content[i][j]) == 120:
            list.append(word)
            word = ""
    if word != '':
        list.append(word)
for i in range(len(list)):
    list[i] = int(list[i])
for i in range(0,len(list), 5):
    changelist(list[i],list[i+1],list[i+2],list[i+3],list[i+4], list_imprim)

#display(list_imprim)
nb_X = howManyX(list_imprim, nb_X)
print("\n" + str(nb_X))



#-------------------------------------------------------------------------------------

def checkAlone(ligne, left, top, tall, wide, list_imprim):
    inter= 0
    for i in range(wide):
        for j in range(tall):
            if list_imprim[top+i][left+j] == 1:
                inter+=1
            else:
                break
    if inter == (wide*tall):
        print(ligne)

for i in range(0,len(list), 5):
    checkAlone(list[i],list[i+1],list[i+2],list[i+3],list[i+4], list_imprim)

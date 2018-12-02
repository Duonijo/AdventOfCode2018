content = open('input.txt', 'r').read().replace('\n',' ')
content = content.split()
#PART ONE
mon_dico = {}
occ = 0
sums_occ2 = 0
sums_occ3 = 0

for i in range(len(content)):
    occ2 = 0
    occ3 = 0
    for j in range(len(content[i])):
        occ = 0
        for k in range(len(content[i])):
            if content[i][j] == content[i][k]:
                occ+=1
        mon_dico[content[i][j]] = occ #appercu par lettres des occurences
        if occ == 2:
            occ2+=1
        elif occ == 3:
            occ3+=1
    if occ2 >= 1:
        sums_occ2+=1
    if occ3 >= 1:
        sums_occ3+=1
result = sums_occ2*sums_occ3
print(result)

#---------------------------------------------------------#

for chaine_x in content:
    for chaine_y in content:
        diff  = 0
        for i in range(len(chaine_x)):
            if chaine_x[i] != chaine_y[i]:
                diff += 1
        if diff == 1:
            result_two = []
            for j in range(len(chaine_x)):
                if chaine_x[j] == chaine_y[j]:
                    result_two.append(chaine_x[j])
result_two = ''.join(result_two)
print(result_two)

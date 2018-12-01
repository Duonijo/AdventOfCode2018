import itertools
content = open('day1input1.txt', 'r').read().replace('\n',' ')

#test avec la liste de l'exemple
list_test = [1, -2, 3, 1]

#PART ONE
sum = 0
list = content.split()
for i in range(len(list)):
   sum += int(list[i])
print(sum)
#La réponse à mon input est 505


#PART TWO

frequence = 0
list_part_two = set([])


for i in itertools.cycle(list):
    frequence += int(i)
    if frequence in list_part_two:
        print(frequence);
        break
    list_part_two.add(frequence)
#La réponse à mon input est 72330

import random

answer = input ('Do you want business lanch or you\'ll choose by yourself? Y(business lanch)/N(manual check) ')

if answer == 'Y' or answer == 'y' or answer == 'Н' or answer == 'н' :
    dishes = '    eGGs ,  spAm, friEd    potatO,   ghrill, souce, mushROOMs , tomato juice, eggs,    Potato   '
    print('Initial data', dishes)
else:
    if answer == 'N' or answer == 'n' or answer == 'Т' or answer == 'т' :
    dishes = input('Enter dishes separated by comma:   ')
   else:
    print('Don\'t cheat me!!! I\'ll prepare the business lanch for you')
    dishes = '    eGGs ,  spAm, friEd    potatO,   ghrill, souce, mushROOMs , tomato juice, eggs,    Potato   '
    print('Initial data ', dishes)

dishes2 = ''

# Words to title
dishes2 = dishes.title()

#Delete spaces
dishes2 = dishes2.replace(' ','')

#Return spaces between words
dishes = dishes2[0:1]
i=1
while i<len(dishes2):
   if (dishes2[i-1]!=',') and (dishes2[i].isupper()):
     dishes = dishes + ' ' + dishes2[i].lower()
     i+=1
   else:
     dishes = dishes + dishes2[i]
     i+=1

#Print in list view
dishes = dishes.split(',')

#from set import Set
dishes = list(set(dishes))
dishes.sort()

max = len(dishes[0])

#Insert '......'
for i in range(len(dishes)):
   b=str(random.randint(1,20))
   dishes[i]= dishes[i]+ '......'+b+'min'
   if len(dishes[i])>max:
     max = len(dishes[i])

print('Your dishes can be served by time:')

#Rows alignment
for i in range(len(dishes)):  
     while len(dishes[i])<max:
        j=dishes[i].index('.')
        dishes[i] = dishes[i][:j+2]+'.'+ dishes[i][j+2:]
     print(dishes[i])


    
    




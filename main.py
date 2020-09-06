# EX0 1
temps = 6.892
distance = 19.7
vitesse  = distance/temps
print(round(vitesse,1))

# EXO 2
age=int(input("saisir un age"))
nom=str(input("sisir un nom"))
print("votre age est", age, "votre nom est", nom)

# EXO 3 
from math import *

flottant= float(input("saisir un flottant"))
if flottant>0 : 
  print(sqrt(flottant))
else : 
  print("ce nest pas positif")
  
#EXO 4
mot1 = str(input("saisir un mot"))
mot2 = str(input("saisir un mot"))

print(min(mot1,mot2))

#EXO 5 

pSeuil = 2.3
vSeuil = 7.41

pressioncourante = float(input("saisir la pression"))
volumecourante = float(input("saisir le volume"))

if pressioncourante>pSeuil and volumecourante>vSeuil :
  print("arret immediat")
elif volumecourante>vSeuil: 
  print("augmenter le volume de l’enceinte")
elif pressioncourante>pSeuil:
  print("diminuer le volume de l’enceinte")
else : 
  print("tout va bien")

##### PARTIE 2 #########
# EXO 6
import re

regex = '^[a-z0-9]+[@]\w+[.]\w{2,3}$'

def mail(email):
  
  if re.search(regex,email):  
      print("cest valide")      
  else:  
      print("ce nest pas valide")
      
#EXO 7
message ="salut"

for i in range(1,11) :
    print(i,message)
    
# EXO 8 

mot1=str(input("rentrer votre mot"))
i=0
#for lettr in mot1:
#print(lettre)
while i<len(mot1): 
  lettre = mot1[i]
  print(lettre)
  i = i + 1

#EX0 9 
a = 0
b = 10

while a < b:
  print(a)
  a = a +1
  
#EXO 10

a = 0
b = 10

while b:
  b = b - 1
  if b % 2 != 0:
    print(b) *
    
#EXO 11
entier = int(input("rentrer un entier entre 1 et 10"))

while (entier>= 1 and entier <=10) :
  entier = int(input("rentrer un entier entre 1 et 10"))
print(entier)

#EXO 13
for i in range(0, 15, 3):
  print(i)
  
#EXO 14 
#Avec for et range
for i in range(0, 12, 2):
  print(i)
  
#EXO 14
#Avec while
entier=12
i=0
while i<entier : 
  if(i%2==0):
    print(i)
  i=i+1
  
###### PARTIE 3 ######

#EXO 15 

liste =[17, 38, 10, 25, 72]
print(" Liste initiale ")
print(liste)
 
liste.sort()
print(liste )

liste.append(12)
print(liste)

liste.reverse()
print(liste)

print(liste.index(17))

liste.remove(38)
print(liste)

print("sous-liste du 2e au 3e élément", liste[1:3])
print("sous-liste du début au 2e élément", liste[:2])
print("sous-liste du 3e élément à la fin de la liste ", liste[2:])
print("sous-liste complète de la liste", liste[:])

#EXO 16 

mot1=str(input("rentrer votre mot"))
i=len(mot1)-1
#for lettre in mot1:
#print(lettre)
while i>=0: 
  lettre = mot1[i]
  print(lettre)
  i = i - 1
  
 #EXO 16 

# Other version with a str empty
mot1 = str(input("rentrer une chaine"))
mot2= ""# chaine vide qui va etre renverse
i = len(mot1) - 1 
while i >= 0 :
    mot2 = mot2 + mot1[i]
    i = i- 1
print(mot2)

# EXO 17 
def palindrome(chaine):
  if(len(chaine)== 0):
    return True
  if (len(chaine)== 1):
    return True

  if chaine[0] == chaine[len(chaine)-1]:
      return palindrome(chaine[1:-1])
  return False  

c = palindrome('kayak')
print(c)

d= palindrome('lol')
print(d)

e = palindrome('bonjour')
print(e)

#EXO 18

import re

regex = '^[a-z0-9]+[@]\w+[.]\w{1,3}$'

def mail2(email):
  
  if re.search(regex,email):  
      print("cest valide")      
  else:  
      print("ce nest pas valide")
      
#EXO 19
truc=[]
machin = [0.0]*5

print(truc)
print(machin)

# EXO 20

for i in range(0,4):
  print(i)
print('\n')
for i in range(4,8):
  print(i)
print('\n')
for i in range(2,10,2):
  print(i)

print('\n')
chose = range(6)
print(chose)
print(3 in chose)
print(6 in chose)

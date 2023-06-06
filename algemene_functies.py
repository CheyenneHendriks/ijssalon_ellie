#Opdracht 2
def mijn_functie_1(item): 
   return pow(item,2)

mijn_lijst_1 = [2, 4, 10, 12]

for item in mijn_lijst_1:
   new_item = mijn_functie_1(item)
   print(new_item)

#Opdracht 3
def mijn_functie_2(item_1, item_2):
   add = int(item_1 + item_2)
   deduct = int(item_1 - item_2)
   multiply = int(item_1 * item_2)
   divide =  int(item_1 / item_2)
   return_waarde = [add, deduct, multiply, divide]
   return return_waarde

mijn_lijst_3 = [(12,3), (12,2), (10,5), (100,20)]
for var_1, var_2 in mijn_lijst_3:
      z = mijn_functie_2(var_1, var_2)
      print(z)




  


import random
from operator import itemgetter

class Dish:
     def _init_(self , name):
        self.dishname = name
		
     def calc_time(self):
	 
	 
	 def to_print(self):
	     print(menu_item)
	     
		 
		 
		
		
		
		
		


input_List = input("Input your favorite dishes (comma separated):\n")

out_dict = {elem.strip().capitalize(): str(random.randint(1,60)) for elem in input_List.split(',') if elem.strip()}

if out_dict:
     print("Can be served:")
     for dish, minutes in sorted(out_dict.items(), key=itemgetter(1)):
         if (len(dish)<14):
                 print(dish + (15-len(dish))*'.' + minutes + 'min')
         else:
                 print(dish + '..' + minutes + 'min')
else:
     print("No dishes ordered.")
	


#-----------------------------------------------------
# Numpy => compare performance and memory usage 
#-----------------------------------------------------
# - performance 
# - memory use 
#-----------------------------------------------------

import numpy as np
import time 
import sys  # عشان حجم العناصر بالباينري 

elements = 150

my_list1 = range (0,elements)
my_list2 = range (0,elements)

my_arrayl = np.arange (elements)
my_array2 = np.arange (elements)

list_start = time.time() # list start بتحسب الوقت عشان ننفذ حاجه 
list_result=[(n1+n2) for n1 , n2 in zip(my_list1,my_list2)] #عملتها ك فاريابل بدل فور لوب 
print(f"List time:{time.time() - list_start }")


# بلووب على اتنين ليست ازا ؟ عن طريق زيب ميثود 
    
#for n1,n2 in zip(my_list1, my_list2):
#    print (n1+n2)

#for n in my_array1 :

#    print (n) # هتطبع الارقام اللي في اليمنتس (من 0 ل 149 )


array_start = time.time()
array_result= my_arrayl + my_array2

print (list_result)

my_array = np.arange(100)

print (my_array)
print(my_array.itemsize) # حجم عناصر البايت 
print(my_array.size) # عدد العناضر اللي جوه ال ارراي ى
print(f"All Bytes :{my_array.itemsize * my_array.size}")

print("#"*50)

my_list = range(100)
print(sys.getsizeof(1))
print(len(my_list))
print(f"All Bytes :{sys.getsizeof(1)* len(my_list) }")
 #Numpy => compare data location and tupe 

import numpy as np 

my_list =[1,2,3,4,5]
my_array = np.array ([1,2,3,4,5])

print (my_list [0])
print (my_list [1])

print ("#"*50)

# id يتجيب الميموري ادريس 

print (id(my_list [0]))
print (id(my_list [1]))

print (id(my_array [0]))
print (id(my_array [1]))

print ("#"*50) 

my_list_of_data = [1,2,"A","B",True,10.50]
my_array_of_data = np.array([1,2,"A","B",True,10.50])

print (my_list_of_data)
print (my_array_of_data)

print ("#"*50) 

print(my_list_of_data[0])
print(my_array_of_data[0])

print (type(my_list_of_data[0]))# هيكون انتجر عشان اول واحد انتجر 
print (type(my_array_of_data[0]))# هيكون استرنج 
# الموضوع ده بيعلمنا الفرق بين ليست و ارراي ان ليست عادي داتا مختلفه لكن ارراي لا 

print ("#"*50) 

my_list_of_data_two = [1,2,"A","B",True,10.50]
my_array_of_data_two = np.array([1,2,])#هتطلع انتجر 
# لو عملتها فلوت هتطلع فلوت بردو عشان الانتجر عادي يكون فلوت انما الفلوت مينفعش يكون انتجر و كذالك مع استرينج 

print (my_list_of_data_two)
print (my_array_of_data_two)

print ("#"*50) 

print(my_list_of_data_two[0])
print(my_array_of_data_two[0])

print (type(my_list_of_data_two[0]))
print (type(my_array_of_data_two[0]))

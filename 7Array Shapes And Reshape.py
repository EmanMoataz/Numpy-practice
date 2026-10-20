#-------------------------------------------
# -- Numpy => Array Shape & Reshape --
#-------------------------------------------
# Shape REturn A 
# Tuple Contains The Number Of Elemente In Each Dimension 
#-------------------------------------------

# عشان نقدر نغير ال array و ال dimensions و عدد العناصر الموجوده فيها 

import numpy as np

my_array1 = np.array ([1,2,3,4])
print (my_array1.ndim) #1
print (my_array1.shape) #(4,)
# shape بترجعلي عدد العناصر اللي موجوده في ال ديمنشن

print ("*"*50)

my_array2 = np.array ([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print (my_array2.ndim) 
print (my_array2.shape) # 3 عناصر و جوه كل واحده 4 عناصر 

print ("*"*50)

my_array3 = np.array ([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]]) # كل [] ب واحد ديمنشن يعني واحد اتجاه 
print (my_array3.ndim) 
print (my_array3.shape)

print ("*"*50)

# Reshape
reshaped_array4 = np.array ([1,2,3,4,5,6,7,8,9,10,11,12])
print (reshaped_array4.ndim) 
print (reshaped_array4.shape)
 
reshaped_array4 =reshaped_array4.reshape(2,6)
print (reshaped_array4.ndim) 
print (reshaped_array4.shape)
print (reshaped_array4)

reshaped_array4 =reshaped_array4.reshape(3,4)
print (reshaped_array4.ndim) 
print (reshaped_array4.shape)
print (reshaped_array4)
 
print ("*"*50)

my_array5 = np.array ([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]])
print (my_array5.ndim) 
print (my_array5.shape)

reshaped_array5 = np.array ([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]])

reshaped_array5 =reshaped_array5.reshape(4,5)
print (reshaped_array5.ndim) 
print (reshaped_array5.shape)
print (reshaped_array5)

print ("*"*50)

reshaped_array5 =reshaped_array5.reshape(5,4)
print (reshaped_array5.ndim) 
print (reshaped_array5.shape)
print (reshaped_array5)

print ("*"*50)

reshaped_array5 =reshaped_array5.reshape(2,5,2)
print (reshaped_array5.ndim) 
print (reshaped_array5.shape)
print (reshaped_array5)

print ("*"*50)
 
reshaped_array5 =reshaped_array5.reshape(-1)
print (reshaped_array5.ndim) 
print (reshaped_array5.shape)
print (reshaped_array5)


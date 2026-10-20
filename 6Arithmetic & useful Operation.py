#-----------------------------------
# -- Arithmetic & useful Operation--
#-----------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Dividation
#----------------------------------
# - min
# - max
# - sum
# - mean (المتوسط) 
# - revel => Returns Flattened Array 1 Dimention With Same Types
#----------------------------------
# - std بقيس مدى تشتت البيانات حول المتوسط 
#----------------------------------
# - ndim بتقولي عدد ال dimentions 
#----------------------------------


import numpy as np 

# Arithmetic operations 
# لازم يكونو نفس السايز

my_array1 = np.array([10,20,30])
my_array2 = np.array([5,2,4])

print (my_array1 + my_array2) # [ , ]
print (my_array1 - my_array2)
print (my_array1 * my_array2)
print (my_array1 / my_array2)

print ("*"*50)

my_array3 = np.array([[1,4],[5,9]])
my_array4 = np.array([[2,7],[10,5]])

print (my_array3 + my_array4) # [ [ n1 , n2 ] , [ n1 , n2 ] ] 
print (my_array3 - my_array4)
print (my_array3 * my_array4)
print (my_array3 / my_array4)

print ("*"*50)

# Min , Max , Sum 

my_array5 = np.array ([10,20,30])
print (my_array5.max())
print (my_array5.min())
print (my_array5.sum())

print ("*"*50)

# 2 Dim

my_array6 = np.array ([[6,4],[3,9]])
print (my_array6.max())
print (my_array6.min())
print (my_array6.sum())

print ("*"*50)

# Ravel
# بتحول ال 2 dim ل 1 dim 


my_array7 = np.array ([[6,4],[3,9]])
print (my_array7.ravel())

my_array8 = np.array ([[[1,2],[3,4]],[[5,6],[7,8]]])

print (my_array8.ndim)
print (my_array8.ravel())
x = my_array8.ravel()
print (x.ndim) 

print ("*"*50)

grades = np.array([80, 90, 75, 60, 95])

print("Average:", np.mean(grades))
print("Highest:", np.max(grades))
print("Lowest:", np.min(grades))
print("Total:", np.sum(grades))

# - Standard Deviation 
# بقيس بيها مدى تشتت البيانات 
# np.std(arr)
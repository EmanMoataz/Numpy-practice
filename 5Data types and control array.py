#------------------------------------------
# -- numpy => Data tupes and control array 
#------------------------------------------

# https://numpy.org/devdocs/user/basics.types.html[cite: 9]
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types[cite: 9]

#------------------------------------------
# "O" (python) objects
# "S" , "a" zero-terminated bytes (not recommended)
# "U" unicode string 
# "V" raw data (void)
#------------------------------------------





import numpy as np 
 
# ازاي نعرف نوع البيانات اللي موجود في ال ارراي 

# show array data type 

my_array1 = np.array([1,2,3])
my_array2 = np.array([1.5,20.15,3.601])
my_array3 = np.array(["Em","Ya","Am"])

# dtype بقدر اعرف منها نوع الداتا اللي جوه ال ارراي 

print (my_array1.dtype)
print (my_array2.dtype)
print (my_array3.dtype)

print ("#"*50)

# ازاي اعمل ارراي بنفسي و احدد البيانات اللي عايزاها 
# creat arrya with specific data type 

my_array4 = np.array([1,2,3], dtype="float") # float , 'float or f 
#float32 , float64 دي ال capacity
my_array5 = np.array([1.5,20.15,3.601], dtype="int")
#my_array6 = np.array(["Em","Ya","Am"],dtype="int")#value error

print (my_array4.dtype)
print (my_array5.dtype)
#print (my_array6.dtype)

print ("#"*50)

#change data type of existing array 

my_array7 = np.array ([0,1,2,3,0,4])
print (my_array7.dtype)
print (my_array7)

print ("#"*50)

my_array7 = my_array7.astype('float')
print (my_array7.dtype)
print (my_array7)

print ("*"*50)

my_array7 = my_array7.astype('bool')
print (my_array7.dtype)
print (my_array7) # true=> , false=>0
 
print ("*"*50)

#test array capacity

my_array8 = np.array ([100,200,300,400],dtype='f')

print(my_array8.dtype)
print(my_array8[0].itemsize) # 4 Bytes

my_array8 = my_array8.astype("float")
print(my_array8.dtype)
print(my_array8[0].itemsize) # 8 Bytes


#--------------------------------------
# Filtering => مهعناها اني بختار كل عنصر بناء على شرط 
#--------------------------------------

import numpy as np 

my_array1 = np.array ([10, 5, 20, 15, 30])

result1 = my_array1 [my_array1 > 15]
print (result1)

print ("*"*50)

grades = np.array ([45,80,30,95,55])

passed = grades[grades>=60]
print (passed)

print ("*"*50)

my_array2 = np.array ([10,20,30,40,50,60,70,80,55,76])

result2 = my_array2 [(my_array2 >= 10) & (my_array2 > 55)]
print (result2)

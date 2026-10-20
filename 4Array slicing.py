#---------------------------
# -- Numpy => Array Slicing
#---------------------------

import numpy as np 

#Slicing => [Start:End:Steps] Not Including End

a = np.array(["A","B","C","D","D","E","F"])

print (a.ndim)#one dimention
print (a[1])
print (a[1:4])
print (a[:4])#مفيش بدايه محدده ف هو هيبدا من الصفر 
print (a[2:])

print ("#"*50)

b = np.array([["A","B","x"],["C","D","y"],["E","F","z"],["M","N","O"]])

print (b.ndim)#one dimention
print (a[1])

print ("#"*50)

# print(b[:3,:2])#اول اتنين في اول تلاته 

print (b[2:,:2])
print (b[2:,:2:2])#هيفوت خطوتين 


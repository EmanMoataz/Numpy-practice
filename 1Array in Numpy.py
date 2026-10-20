# numpy => creat arrays  

import numpy as np #ده استدعاء نمباي 
# np ده اسم نبماي بدل ما كل شويه اكتب اسمها كامل 

my_list =[1,2,3,4] # دي ليست عادي
my_array = np.array(my_list) # حولنا الليست ل ارراي 


print(my_list) # هتطبع الليست عادي 
print (my_array) # هتنطبع ك ارراي 
# اخلي بالي ان اللي بيفرق هي الكمه بس 

print ("#"*50)

print(type(my_list)) # ده تعريف نوع الليست 
print (type(my_array)) # تعريف نوع ال ارراي 
 # هيظهرلي ndarray معناها يعني مصفوفه بوجهين بس مختصره 

 #ِAccessing Elements 
print (my_list [0])
print (my_array [0])

print ("#"*50)

a=np.array(10)
b=np.array([10,20]) 
c=np.array([[1,2],[3,4]])
d=np.array( [ [ [5,6] , [7,9]] ,[ [1,3],[4,8] ] ]) # 3 dimentional array 
print (d[1][1][1]) #هيطبع رقم 8
print (d[1,1,-1]) # اخر اندكس ممكن اقول عليه -1 

print ("#"*50)

# Number of dimentions 
# عدد الاقواس هو هو عدد الديمنشنز 

print (a.ndim)
print (b.ndim)
print (c.ndim)
print (d.ndim)

# custom dimention مصفوفه بعدد ابعاد مخصص 

my_custom_array = np.array ([1,2,3], ndmin=3 )
print (my_custom_array)
print (my_custom_array.ndim)
print (my_custom_array[0,0,0])
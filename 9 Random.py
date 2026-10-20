#---------------------------
# -- Random -
#---------------------------

# --rand () => ارقام عشريه 
# --randint () => ارقام صحيحه 

#--------------------------- 
# بستخدمها عشان اعمل ارقام عشوائيه و دي مهمه في data scince , machine learning

import numpy as np 
x = np.random.rand ()
print (x)

print ("*"*50)

# مجموعة ارقام عشوائيه

y = np.random.rand(5)
print (y) # هتنطبع في شكل array 

print ("*"*50)

#  

z = np.random.randint (1,10,5) 

# 1=> the begining
# 10 => النهايه غير شامله 
# 5 => عدد الاقام 

print (z)

print ("*"*50)

# Random Matrix 

e = np.random.randint(1,10,(3,4))
print (e)

# 1 , 10  => بيحددو نطاق الارقام 
# 3 , 4 => 3 رو و اربعه كولوم 

print ("*"*50)


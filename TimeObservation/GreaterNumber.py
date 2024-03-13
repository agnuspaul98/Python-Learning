import time

s1 = time.time()
a,b=4,5
if(a>b):
    print("{} is greater than {}".format(a,b))
else:
    print("{} is greater than {}".format(b,a))

e1=time.time()
print ("The time of execution of above program is :",
       (e1-s1) * 1000, "ms")

s2=time.time()
i1=input("Enter first number:")
i2=input("Enter second number:")
if(i1>i2):
    print("{} is greater than {}".format(i1,i2))
elif(i2<i1):
    print("{} is greater than {}".format(i2,i1))
else:
    print("{} is equal to {}".format(i1,i2))

e2=time.time()
print ("The time of execution of above program is :",
       (e2-s2) , "s")
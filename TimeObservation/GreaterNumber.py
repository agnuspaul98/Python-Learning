import time

s1 = time.time()
a,b=5,5
if(a>b):
    print("{} is greater than {}".format(a,b))
elif(a<b):
    print("{} is greater than {}".format(b,a))
else:
    print("{} is equal to {}".format(a,b))

e1=time.time()
p1=(e1-s1) * 1000
print ("The time of execution of above program is :",
       p1, "ms")

s2 = time.time()
c,d=5,10
print(max(c,d))
e2=time.time()
p2=(e2-s2) * 1000
print ("The time of execution of above program is :",
       p2, "ms")


s3=time.time()
i1=input("Enter first number:")
i2=input("Enter second number:")
if(i1>i2):
    print("{} is greater than {}".format(i1,i2))
elif(i1<i2):
    print("{} is greater than {}".format(i2,i1))
else:
    print("{} is equal to {}".format(i1,i2))

e3=time.time()
p3=(e3-s3)*1000
print ("The time of execution of above program is :",
       p3 , "ms")

pList=[p1,p2,p3]
print(sorted(pList))

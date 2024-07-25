#to print fibonacci series upto n

n=int(input("enter limit:"))
i=1
sum=0

first=0
second=1
print(first)
print(second)

while(i<=n-2):
    sum=first+second
    print(sum)
    first=second
    second=sum
    i+=1





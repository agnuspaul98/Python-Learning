#Print the factorial of a number
n=int(input("Enter the number:"))
f=1
while(n>=1):
    f=f*n
    n-=1
print(f)
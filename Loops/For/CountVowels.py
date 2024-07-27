y='y'
while (y=='y'):
    str_input= input("Enter String:")
    count=0
    vowels=[]
    for i in str_input:
        if(i.lower() in ('a','e','i','o','u')):
         count=count+1
         vowels.append(i)


    print(count)
    print("The vowels are:", ", ".join(vowels))
    y=input("Do you want to continue?(y/n)")



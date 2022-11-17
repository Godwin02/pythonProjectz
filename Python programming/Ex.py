x=int(input("Enter  starting year: "))
y=int(input("Enter  ending year: "))
print("The following are the leap years.")
for i in range(x,y):

   if((i%400==0)or ((i%100!=0)and (i%4==0))):
       print(i)








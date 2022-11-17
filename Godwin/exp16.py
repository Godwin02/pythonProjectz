list=[]
n=int(input("enter the number of elements"))
print("Enter the elements")
for i in range(0,n):
    ele=int(input())
    if(ele>100):
        list.append("over")
    else:
        list.append(ele)
print(list)
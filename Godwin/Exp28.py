def factor(i):
    print("Enter a number:",i)
factor(i=" x=")
x=int(input( ))
print("Factors of x are:")
for j in range(1,x):
    if x%j==0:
        print(j ,end=",")


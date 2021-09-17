from  random import  randint

n =int(input("N :"))
a =[[randint(1,100) for i in range(n)] for j in range(n)]
for i in range(n):
    print(*a[i])

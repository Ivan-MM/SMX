entrada     salida
5,5            5 5
5,1            1 5  
1,5            5 1

n1=int(input("introduce un número cualquiera"))
n2=int(input("introduce un número cualquiera"))
if(n1>n2):
    n3=n2
    n2=n1
    n1=n3
print(n1,n2)

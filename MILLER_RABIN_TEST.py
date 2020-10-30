#MILLER_RABIN  TEST
n=int(input('Enter a number: '))
r=n-1
m=n-1
k=0
while m%2==0:
        k=k+1
        m=m/2
if n==1:
    print('1 is nither prime nor composite')
elif n==2:
    print('it is prime')
   
   
# using miller_rabin test for the remaining numbers
else:
    a=2 
    j=(a**m)%n
    
    if j==1:
        print(str(n) + " is probably prime.")
    elif j==-1:
        print(str(n) + " is probably prime.")
    else:
        i=1
        while i in range(0,k):
            j=(a**((2**i)*m))%n
            i=i+1
            
            if j==n-1:
                
                break
            

        if j%n!=n-1:
            print(str(n) + " is composite.")
        else:
            print(str(n) + " is probably prime.")

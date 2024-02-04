n=int(input())
ans=1
if n==0:
    print(1)
elif n<0:
    print("error")
else:
    for i in range(1,n+1):
        ans=ans*i
    print(ans)

# question
    x,n=input().split()
    x=int(x)
    n=int(n)
    ans=1
    for i in range(n):
        ans=ans*x
    print(ans)


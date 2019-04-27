T=int(input())
for x in range(T):
    a=int(input())
    A=set(map(int,input().split()))
    b=int(input())
    B=set(map(int,input().split()))
    if a>b:
        print("False")
    elif A.intersection(B)==A:
        print("True")
    else:
        print("False")


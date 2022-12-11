N=list(map(int,input("Enter 5 positive numbers").split()))
if(N[0]<=0) or(N[1]<=0) or (N[2]<=0) or(N[3]<=0) or(N[4]<=0):
    print("enter only positive numbers")
else:
    print(sum(N))
def median(A,B):
    n=len(A); l,r=0,n
    while l<=r:
        i=(l+r)//2; j=n-i
        A1=A[i-1] if i>0 else -10**9
        A2=A[i] if i<n else 10**9
        B1=B[j-1] if j>0 else -10**9
        B2=B[j] if j<n else 10**9
        if A1<=B2 and B1<=A2:
            return (max(A1,B1)+min(A2,B2))/2
        elif A1>B2: r=i-1
        else: l=i+1

A=[1,3,5]; B=[2,4,6]
print("Median =", median(A,B))

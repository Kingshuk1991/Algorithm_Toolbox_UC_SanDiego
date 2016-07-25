# Uses python3
def edit_distance(s,t):
    L1=len(s)
    L2=len(t)
    A =[[0 for i in range(L2+1)] for j in range(L1+1)]
    for i in range(0,L2+1):
        A[0][i]=i
        
    for i in range(0,L1+1):
        A[i][0]=i
    #print (A[0][0])
    #print (A[0][5])
    #print (A[4][0])
    #print (A)
    for i in range(1,L1+1):
        for j in range(1,L2+1):
            k=0 if s[i-1]==t[j-1] else 1
            A[i][j]=min(A[i][j-1]+1,A[i-1][j]+1,A[i-1][j-1]+k)
            #print ('The possible values '+ str(A[i][j-1]+1)+ ' and '+ str(A[i-1][j]+1)+ ' and '+str(A[i-1][j-1]+k))
            #print ('Optimal Value is '+str(A[i][j]))
            #print (A)
    return A[L1][L2]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

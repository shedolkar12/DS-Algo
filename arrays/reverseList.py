A = [[1, 2, 3, 4], [5, 6, 7, 8]]

def reverse(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0]*n)
        for j in xrange(len(A[i])):
            B[i][n-1-j] = A[i][j]
    
    return B        

print reverse(A)

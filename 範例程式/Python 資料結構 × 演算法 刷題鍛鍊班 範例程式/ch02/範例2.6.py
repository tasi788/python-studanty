def printMatrix(A):
  for i in range(len(A)):		#照顧矩陣每一列，由i走訪
    for j in range(len(A[i])):		#照顧第i列的每一個元素，寫A[0]也可以
      print(A[i][j], end = ' ')  
    print()					#印完一列要換行
def addMatrix(A, B, C):
  for i in range(len(A)):		#照顧矩陣A,B每一列
    for j in range(len(A[0])):	#照顧矩陣A,B第i列的每一行
      C[i][j] = A[i][j] + B[i][j]

A = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
B = [[1,1,1], [1,1,1], [1,1,1], [1,1,1]]
C = [[0]*len(A[0]) for _ in range(len(A))]
addMatrix(A, B, C)
printMatrix(C)
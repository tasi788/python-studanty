def printMatrix(A):
  for i in range(len(A)):		#照顧矩陣每一列，由i走訪
    for j in range(len(A[i])):		#照顧第i列的每一個元素，寫A[0]也可以
      print(A[i][j], end = ' ')  
    print()					#印完一列要換行
def multiplyMatrix(A, B, C):
  for i in range(len(A)):			#A的每一列
    for j in range(len(B[0])):		#B的每一行
      C[i][j] = 0
      for k in range(len(A[0])):		# A的行數（B的列數）
        C[i][j] += A[i][k] * B[k][j]

A = [[1,2], [3,4], [5,6]]
B = [[0,1,1,2], [4,0,-1,3]]
C = [[0]*len(B[0]) for _ in range(len(A))]   # C大小= A的列數 B的行數
printMatrix(A)
printMatrix(B)
multiplyMatrix(A, B, C)
printMatrix(C)
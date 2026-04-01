class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 123 741
        # 456 852
        # 789 963
        import numpy as np
        # x = np.array([[1,2,3],[4,5,6],[7,8,9]])
        # print(x, x.T)
        # 0,0->0,2; 0,2->2,2; 2,2->2,0; 2,0->0,0
        # 0,1->1,2; 1,2->2,1; 2,1->1,0; 1,0->0,1
        # i,j->j,n-i; j,n-i->n-i,n-j; n-i,n-j->n-j,i; n-j,i->i,j
        # matrix = np.array(matrix)
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n-1-i):
                tmp = matrix[j][n-i-1] 
                matrix[j][n-i-1] = matrix[i][j]
                tmp2 = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = tmp
                tmp = matrix[n-1-j][i]
                matrix[n-1-j][i] = tmp2
                matrix[i][j] = tmp

                # print(i,j, matrix)
        # matrix = matrix.tolist()
        # print(matrix)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import numpy as np
        import bisect
        def binary_search_bisect(arr, x):
            # Find the leftmost insertion point for x
            i = bisect_left(arr, x)
            if i != len(arr) and arr[i] == x:
                return i
            return -1

        matrix = np.array(matrix)
        row = bisect.bisect_left(matrix[:,-1], target)
        # if row!=matrix.shape[0]-1:
        #     row += 1
        if row == matrix.shape[0]:
            row -=1
        print(row)
        column = bisect.bisect_left(matrix[row,:], target)
        if column == matrix.shape[1]:
            column-=1
        print(column)
        if (matrix[row, column]==target):
            return True
        return False

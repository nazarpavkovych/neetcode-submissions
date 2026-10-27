class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix)-1
        while l_row<=r_row:
            mid_row = (r_row+l_row)//2
            if matrix[mid_row][0]<=target and matrix[mid_row][-1]>=target:
                break
            if matrix[mid_row][0]<target:
                l_row=mid_row+1
            if matrix[mid_row][0]>target:
                r_row=mid_row - 1
            if matrix[mid_row][0] == target:
                return True
        print(mid_row)
        l_col = 0
        r_col = len(matrix[mid_row])-1
        while l_col<=r_col:
            mid_col = (r_col+l_col)//2
            if matrix[mid_row][mid_col]<target:
                l_col= mid_col+1
            if matrix[mid_row][mid_col]>target:
                r_col = mid_col-1

            if matrix[mid_row][mid_col]==target:
                return True
        return False

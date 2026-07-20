class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=(l+r)//2
            row=mid//n
            col=mid%n
            value=matrix[row][col]
            if value==target:
                return True
            elif value>target:
                r=mid-1
            else:
                l=mid+1
        return False 

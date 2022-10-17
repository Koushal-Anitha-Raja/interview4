#time complexity :o(n logn)
#sppace complexity:o(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #assigning the length value to matrix
        m=len(matrix)
        #iterate it through the loop 
        for i in range(m):
            #finding the middle element and assigning low as zero
            low=0
            high=len(matrix[0])-1
            #usual binary search condition until low is greater than high
            while(low<=high):
                mid=low+(high-low)//2
                #if my target value equals to mid then
                if target==matrix[i][mid]:
                    return True
               #if my target value less than mid
                elif target<matrix[i][mid]:
                    high=mid-1
                #or else do 
                else:
                    low=mid+1
        #if none of the cases is true return false        
        return False      
            
   
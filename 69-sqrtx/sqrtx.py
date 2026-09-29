class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid  # Perfect match, return immediately
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
                
        # If no perfect match was found, 'right' holds the rounded-down answer
        return right
            


        
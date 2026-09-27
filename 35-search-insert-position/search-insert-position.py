class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        c=0
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i<target:
                    c+=1
            return c
        
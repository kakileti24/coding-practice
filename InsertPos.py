from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bs(nums, low, high, target):
            if low > high:
                return low
            
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bs(nums, mid + 1, high, target)
            else:
                return bs(nums, low, mid - 1, target)
        
        return bs(nums, 0, len(nums) - 1, target)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0 
        j=1
        while True:
            if nums[i]+nums[j]== target:
                return [i,j]
            elif  j<=len(nums)-2:
                j+=1
                
            else:
                i+=1
                j=i+1
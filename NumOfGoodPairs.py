class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
       c={}
       res=0
       for i in nums:
        if i in c:
            res+=c[i]
            c[i]+=1
        else:
            c[i]=1
       return res
            
            
        
        
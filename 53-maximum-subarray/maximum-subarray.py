class Solution(object):
    def maxSubArray(self, nums):
       cs = nums[0]
       ms = nums[0]
       for num in nums[1:] :
            cs = max(cs+num , num)
            ms = max(ms , cs)
       return ms
    
        
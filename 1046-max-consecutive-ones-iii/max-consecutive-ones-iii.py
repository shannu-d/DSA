class Solution(object):
    def longestOnes(self, nums, k):
        l = 0 
        r = 0 
        ml = 0
        n = len(nums)
        zeroes = 0 
        while r < n :
            if nums[r] == 0 :
                zeroes += 1
            if zeroes > k :
                if nums[l] == 0 :
                    zeroes -= 1
                l += 1
            if zeroes <= k : 
                ml = max(ml , r - l + 1)
            r += 1 
        return ml

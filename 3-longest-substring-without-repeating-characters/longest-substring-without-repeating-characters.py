class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        ml = 0 
        n = len(s)
        hash_arr = [-1]*256
        while r < n :
            if hash_arr[ord(s[r])] != -1:
                if hash_arr[ord(s[r])] >= l:
                    l = hash_arr[ord(s[r])] + 1
            ml = max(ml , r-l+1 )
            hash_arr[ord(s[r])] = r
            r += 1
            
        return ml
        
class Solution(object):
    def characterReplacement(self, s, k):
        l =0 
        r = 0 
        ml = 0 
        maxf = 0 
        hash_arr = [0]*26
        n = len(s)

        while r < n:

            hash_arr[ord(s[r])-ord('A')] += 1
            maxf = max(maxf , hash_arr[ord(s[r])-ord('A')] )

            if (r-l+1) - maxf > k:
                hash_arr[ord(s[l])-ord('A')] -= 1
                l += 1

            if (r-l+1) - maxf <= k:
                ml = max (ml , (r-l+1))

            r += 1

        return ml 
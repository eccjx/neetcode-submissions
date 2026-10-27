class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        set_ = set()
        curr_len = 0
        for right in range(len(s)):
            if s[right] not in set_:
                set_.add(s[right])
                
            else:
                res = max(len(set_), res)
                while s[left] != s[right]:
                    set_.remove(s[left])
                    left += 1
                    
                left += 1
        res = max(len(set_), res)
        return res
                



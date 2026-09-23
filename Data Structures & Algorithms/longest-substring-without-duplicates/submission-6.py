class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = 0
        current_len = 0
        seen_set = set()
        for right in range(len(s)):
            if s[right] not in seen_set:
                seen_set.add(s[right])
                current_len += 1
                res = max(res, current_len)
            else:
                while s[l] != s[right]:
                    seen_set.remove(s[l])
                    current_len -= 1
                    l += 1
                l += 1
        return res
                
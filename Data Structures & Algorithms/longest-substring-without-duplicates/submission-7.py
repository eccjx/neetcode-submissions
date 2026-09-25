class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen_set = set()
        for r in range(len(s)):
            if s[r] not in seen_set:
                seen_set.add(s[r])
                current_len = len(seen_set)
                res = max(res, current_len)
            else:
                while s[l] != s[r]:
                    seen_set.remove(s[l])
                    l += 1
                l += 1
        return res
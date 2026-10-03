class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        r = 0
        l = 0
        max_len = 0
        cur_len = 0
        for r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
                cur_len += 1
            else:
                max_len = max(max_len, len(char_set))
                while s[l] != s[r]:
                    char_set.remove(s[l])
                    l += 1 
                l += 1
        max_len = max(max_len, len(char_set))
        return max_len

        

       
        
            
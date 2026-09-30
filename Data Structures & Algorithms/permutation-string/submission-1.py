class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = defaultdict(int)
        for char in s1:
            char_dict[char] += 1
        
        l = 0
        r = len(s1) - 1
        char_2 = defaultdict(int)
        
        for char in s2[:(r+1)]:
            if char in char_dict:
                char_2[char] += 1
        print(char_2)
        if char_2 == char_dict:
            return True
        
        while r <= len(s2) - 2:
            if s2[l] in char_dict:
                char_2[s2[l]] -= 1
            l += 1
            r += 1
            if s2[r] in char_dict:
                char_2[s2[r]] += 1
            if char_2 == char_dict:
                return True
        return False
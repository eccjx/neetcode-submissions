class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x if x.isalnum() else "" for x in s]
        clean_s = "".join(s).lower()
        left = 0
        right = len(clean_s) - 1
        while left <= right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        
        return True

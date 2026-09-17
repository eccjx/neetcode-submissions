class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([char for char in s if char.isalnum()]).lower()
        for i in range(len(clean_s)):
            other_i = len(clean_s) - i - 1
            if other_i < i:
                break
            if clean_s[i] != clean_s[other_i]:
                return False
            
        return True
         

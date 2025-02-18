class Solution:
    def isPalindrome(self, s: str) -> bool:
        # I need to clear or ignore all special characters
        s = s.lower()
        clean_str = ""

        for char in s:
            if char.isalnum():
                clean_str += char

        length = len(clean_str)
        for i in range(length):
            if(i > length / 2): 
                break
            if(clean_str[i] != clean_str[length - 1 - i]):
                return False
        return True
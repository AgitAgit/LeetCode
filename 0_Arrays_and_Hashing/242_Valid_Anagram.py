# Given two strings s and t, return true if t is an 
# anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashS = {}
        hashT = {}
        for i in range(len(s)):
            # Fill the s dictionary
            if s[i] in hashS:
                hashS[s[i]] += 1
            else:
                hashS[s[i]] = 1

            # Fill the t dictionary
            if t[i] in hashT:
                hashT[t[i]] += 1
            else:
                hashT[t[i]] = 1
        
        for key in list(hashS.keys()):
            if not key in hashT:
                return False
            if not hashS[key] == hashT[key]:
                return False
        
        return True
# Time complexity O(n^2)
class Solution:
    # Time complexity: 2s + t = O(s)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        obj1 = {}
        for char in s:
            if char in obj1:
                obj1[char] += 1
            else: 
                obj1[char] = 1
        for char in t:
            if char not in obj1:
                return False
            obj1[char] -= 1
        for char in obj1:
            if obj1[char] != 0:
                return False
        return True
    
    # Time complexity O(n^2)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # groups = [[strs[0]]]
        # for word in strs:
        groups = {} # f"{strs[0]}" : []

        for word in strs:
            category_found = False

            for group in groups:
                # Time complexity: group = O(group)
                if self.isAnagram(group, word):
                        groups[group].append(word)
                        category_found = True
            if not category_found:
                groups[word] = [word]
        # print(groups)

        result = []
        for group in groups:
            result.append(groups[group])
        return result    
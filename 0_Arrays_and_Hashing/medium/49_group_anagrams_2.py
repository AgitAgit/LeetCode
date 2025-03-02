class Solution:
    def convert_char_to_place(self, char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        else:
            return None

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                place = self.convert_char_to_place(char)
                count[place] += 1
            category = str(count)
            if category in groups:
                groups[category].append(word)
            else:
                groups[category] = [word]
        
        result = []
        
        for category in groups:
            result.append(groups[category])

        return result
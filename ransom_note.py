
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        string = ""
        hash_map = {}
        for i in range(len(magazine)):
            hash_map[magazine[i]] = magazine[i]
        
        for letter in ransomNote:
            if hash_map.get(letter) != None:
                string += hash_map.pop(letter)
        print(string)
        return string == ransomNote


s = Solution()
s.canConstruct("aa","aab")
print(s)
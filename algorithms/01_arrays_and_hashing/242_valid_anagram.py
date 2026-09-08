class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = dict()
        for letter in s:
            count[letter] = count.get(letter, 0) + 1
        for letter in t:
            if letter not in count:
                return False
            count[letter]-=1
            if count[letter]<0:
                return False
        return True   
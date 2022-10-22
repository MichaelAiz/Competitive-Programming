class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashbrown = {}
        for letter in s:
            if letter in hashbrown:
                hashbrown[letter] += 1
            else:
                hashbrown[letter] = 1
        for letter in t:
            if letter in hashbrown:
                hashbrown[letter] -= 1
            else: 
                return False
        for val in hashbrown.values():
            if val != 0:
                return False
        return True
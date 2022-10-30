class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        odd = 0
        total = 0
        for letter in letters:
            if letters[letter] % 2 == 0:
                total += letters[letter]
            else:
                total += letters[letter] - 1
                odd = 1
        return total + odd
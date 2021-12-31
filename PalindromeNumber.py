class Solution:
    def isPalindrome(self, x: int) -> bool:
        backwordsNum = 0
        count = 0
        temp = x
        while x > -1:
            backwordsNum *= 10
            backwordsNum += x % 10
            x //= 10
            if backwordsNum == temp:
                return True
            elif backwordsNum > temp or backwordsNum == 0:
                return False
        return False
            
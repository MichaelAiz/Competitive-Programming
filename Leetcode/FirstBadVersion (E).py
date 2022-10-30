class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        firstBad = n
        while first <= last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                firstBad = mid
                last = mid - 1
            else:
                first = mid + 1
        return firstBad
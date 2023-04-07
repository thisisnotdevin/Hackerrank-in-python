class Solution(object):
    def findClosestNumber(self, nums):
        pos = 999999
        neg = -pos
        for x in nums:
            if x < 0:
                if x > neg:
                    neg = x
            elif x < pos:
                pos = x
        return pos if pos <= -neg else neg

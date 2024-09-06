# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

#use binary search

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while (low <= high):
            mid = (low + high) / 2
            if(guess(mid) < 0):
                high = mid - 1
            elif (guess(mid) > 0):
                low = mid + 1
            else:
                return mid
        
        return -1
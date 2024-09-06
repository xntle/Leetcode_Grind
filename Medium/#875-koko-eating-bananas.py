class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        maxN = max(piles)
        l = 1
        high = maxN

        while (l <= high):
            k = (l + high) // 2

            total_hours_used = 0
            for p in piles:
                total_hours_used += math.ceil(float(p)/k)
            
            if(total_hours_used <= h):
                res = k 
                high = k - 1
            else:
                l = k + 1
        
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        start best = 0
        keep a global min
        loop through arr, if a val is higher than min
         best = max(best, higher - g_min)
        
        return best
        '''

        best = 0
        g_min = float('inf')
        for i in range(len(prices)):
            if prices[i] < g_min:
                g_min = prices[i]
            else:
                best = max(best, prices[i] - g_min)

        return best
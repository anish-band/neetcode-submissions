class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        need to store coutns of each var in window
        also need to store the highest freq char in the window
        
        window is valid when len(window) - highest_freq <= k
        use right pointer to increment:
            update s[r] count, update max_freq with whatever the max_freq is
        
        it the window condition is violated:
            shrink using left pointer, and update counts asw

        compute window size
        return
        '''

        counts = {}
        highest_freq = 0
        res = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            highest_freq = max(highest_freq, counts[s[r]])
            while (r - l + 1) - highest_freq > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

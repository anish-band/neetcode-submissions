class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        keep a global max
        use a dynamic window (through a pointers and a set)
        left pointer starts at beginning of str, right starts at left
        while char at r doesnt equal char at l, add to window (calc best on adds)
        when char at r is already in window remove char at l, increment l until char at r is valid

        return best
        '''

        best = 0
        window = set()
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            best = max(best, r - l + 1)
        return best

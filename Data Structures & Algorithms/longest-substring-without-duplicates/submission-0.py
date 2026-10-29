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
        l , r = 0, 0
        while r < len(s):
            while r < len(s) and s[r] not in window:
                window.add(s[r])
                r += 1
            best = max(best, len(window))

            if r == len(s):
                break
            
            while s[l] != s[r]:
                window.remove(s[l])
                l += 1
            window.remove(s[l])
            l += 1
        return best

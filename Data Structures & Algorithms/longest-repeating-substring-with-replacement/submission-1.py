class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        first determine highest freq char
        store a best var and modified var
        while pointer < len(s):
            if its the highest freq char, add to len count,
            if not:
                if modified < k:
                 (modified++ and len_count++)
        '''

        counts = {}
        max_count = -1
        highest_char = '0'
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            if (counts[c] > max_count):
                max_count = counts[c]
                highest_char = c
        
        modified = 0
        l = 0
        highest_len = -1
        for r in range(len(s)):
            if s[r] != highest_char and modified < k:
                modified += 1
            elif s[r] != highest_char and modified >= k:
                while modified >= k:
                    if s[l] != highest_char:
                        modified -= 1
                    l += 1

            highest_len = max(highest_len, r - l + 1)

        return highest_len
        
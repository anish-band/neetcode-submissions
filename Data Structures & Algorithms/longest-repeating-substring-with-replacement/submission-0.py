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
        
        counter = 0
        l = 0
        window = []
        highest_len = -1
        for r in range(len(s)):
            if s[r] == highest_char:
                window.append(s[r])
            elif counter < k:
                window.append(s[r])
                counter += 1
            else:
                while counter >= k and l < len(window):
                    removed_c = window.pop(l)
                    if removed_c != highest_char:
                        counter -= 1
                    l += 1
                window.append(s[r])

            highest_len = max(highest_len, len(window))

        return highest_len
        
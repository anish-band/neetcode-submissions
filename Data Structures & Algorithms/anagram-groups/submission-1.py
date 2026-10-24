class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        map where key is 26 array and value is a list of words
        that match the key

        turn list into a tuple to make it hashable

        loop through strs:
            create key
            add str to the list for that key

        return the values of the map in a list
        '''

        str_chars = {}

        for str in strs:
            char_counts = [0] * 26
            for char in str:
                char_counts[ord(char) - ord("a")] += 1;

            char_key = tuple(char_counts)
            if char_key not in str_chars:
                str_chars[char_key] = []
            
            str_chars[char_key].append(str)

        return list(str_chars.values())






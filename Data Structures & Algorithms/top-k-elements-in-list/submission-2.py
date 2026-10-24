class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        map where key is count and val is list of nums that have that

        max freqs go from 0 -> len(nums)

        so first figure out counts of each num (store in map)
        then loop through the map, and use the value as key for a second
        map where val is a list and put num in there

        loop from the end of the list until u hit k 

        '''

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freqs = [[] for i in range(len(nums) + 1)]
        for num, cnt in counts.items():
            freqs[cnt].append(num)

        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if (len(res) == k):
                    return res
    
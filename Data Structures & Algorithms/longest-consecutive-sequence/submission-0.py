class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        first turn nums into a set
        
        make a best var, and a counter var
        then loop through the set (each element is n):
            if n - 1 is in set continue
            otherwise, while n + 1 is in set, counter goes up
            check max each time 

        return max
        '''

        nums_set = set(nums)
        best = 0

        for n in nums_set:
            if (n - 1 in nums_set):
                continue
            
            counter = 1
            while (n + 1 in nums_set):
                n += 1
                counter += 1

            best = max(best, counter)

        return best

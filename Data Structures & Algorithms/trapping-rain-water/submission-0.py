class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        2 pointers starting on opposite sides
        store lmax and rmax:
            everytime u move a height, if its less that its respective max, theres water above it
        traverse logic (while l < r):
            total += max - height[l/r]
            move min(l, r) up/down
            
        '''

        total = 0
        n = len(height)
        l_max, r_max = 0, 0
        l_height, r_height = 0, 0
        l, r = 0 , n - 1

        while l < r:
            l_height, r_height = height[l], height[r]
            l_max, r_max = max(l_height, l_max), max(r_height, r_max)

            if l_height < r_height:
                total += l_max - l_height
                l += 1
            else:
                total += r_max - r_height
                r -= 1
        return total


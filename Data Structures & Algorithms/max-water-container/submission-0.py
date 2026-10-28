class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        2 pointers left starts at 0 right at end
        best = 0
        width is just r - l
        height is min(l, r)
        area = width * height
        update best at every area calc

        traverse by;
            moving min(l, r) up
        '''
        best_area = 0
        n = len(heights)
        l, r = 0, n - 1

        while l < r:
            width = r - l
            min_height = min(heights[l], heights[r])
            area = width * min_height
            best_area = max(area, best_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return best_area

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        2 pointers left and right
        while left is less than right:
            if the sum is too small:
                left goes up
            else if too big right goes down
            else: return indices + 1
        '''


        l , r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

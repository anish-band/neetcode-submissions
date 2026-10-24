class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        '''
        n = len(nums) * 2
        ans = [0] * n

        for traverse < n:
            ans[traverse] = 


        '''

        n = len(nums) * 2
        
        ans = [0] * n

        for i in range(n):
            if (i < len(nums)):
                ans[i] = nums[i]
            else:
                ans[i] = nums[i - len(nums)]

        return ans
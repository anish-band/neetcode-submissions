class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        create output arr

        create l->r sum (lr)
        first pass fill with only product of nums to the left:
            lr starts at 1, each pass multiply by num[i]
            output[i] = lr


        create r->l sum (rl) and set it to equals nums[n -1] 
        second pass go from n - 2 to 0, and do products of the right
        
        return output
        '''
        
        n = len(nums)
        output = [1] * n
        
        lr = 1
        for i in range (n):
            output[i] = lr
            lr *= nums[i]
        
        rl = 1
        for i in range (n - 1, -1, -1):
            output[i] *= rl
            rl *= nums[i]

        return output

        
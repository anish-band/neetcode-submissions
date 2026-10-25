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
        output = [0] * n
        lr = 1
        output[0] = 1
        for i in range (1, n):
            lr *= nums[i - 1]
            output[i] = lr
        
        rl = 1
        for i in range (n - 2, -1, -1):
            rl *= nums[i + 1]
            output[i] = output[i] * rl

        return output

        